import os
# Avoid automatic extra parallelization by other modules
os.environ['OMP_NUM_THREADS'] = "1"
os.environ['OPENBLAS_NUM_THREADS'] = "1"
os.environ['MKL_NUM_THREADS'] = "1"
os.environ['VECLIB_MAXIMUM_THREADS'] = "1"
os.environ['NUMEXPR_NUM_THREADS'] = "1"


import click
import logging
import numpy as np
from pathlib import Path

from src.array_handler import load_mcw_arrays_from_input_dir
from src.dataloader import load_and_extract, save_as_fits
from src.prob import get_field_and_memb_likelihoods, get_probability


@click.command()
@click.option("-f", help="Input fits file", required=True)
@click.option("-o", help="Output fits file", required=True)
@click.option("-p", help="GMM parameters dir", default="gmm_params/pm+par_7comp/")
@click.option("-ps", help="Parameter space (pm+parallax, pm_only, pm+parallax_tf3, pm_only_tf3)", default="pm+parallax")
@click.option("-bs", help="Batch size", type=int, default=100_000)
@click.option("--prob", help="Compute total probabilities", is_flag=True, default=False)
def main(f, o, p, prob, ps, bs):
    
    # Initialize logger
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logfile.txt",
        level=logging.DEBUG,
    )
    logging.info("--Program Started--")
    logging.info(f"Input file: {f}")
    logging.info(f"Output file: {o}")
    
    # Inputs
    input_file, output_file = Path(f), Path(o)
    gmm_params_dir = Path(p)
    
    if not input_file.exists():
        logging.error("Input file does not exist")
        raise FileNotFoundError("Input file does not exist")
    
    if output_file.exists():
        logging.error("Output file already exists")
        raise FileExistsError("Output file already exists")
    
    if not gmm_params_dir.exists():
        logging.error("GMM parameters directory does not exist")
        raise FileNotFoundError("GMM parameters directory does not exist")
    
    ps = ps.lower()
    logging.info(f"Parameter space: {ps}")
    match ps:
        case "pm+parallax":
            data_columns = ["pmra", "pmdec", "parallax"]
            errors_columns = ["pmra_error", "pmdec_error", "parallax_error"]
        case "pm_only":
            data_columns = ["pmra", "pmdec"]
            errors_columns = ["pmra_error", "pmdec_error"]
        case "pm+parallax_tf3":
            data_columns = ["pmra_corr_tf3", "pmdec_corr_tf3", "parallax"]
            errors_columns = ["pmra_error", "pmdec_error", "parallax_error"]
        case "pm_only_tf3":
            data_columns = ["pmra_corr_tf3", "pmdec_corr_tf3"]
            errors_columns = ["pmra_error", "pmdec_error"]
        case _:
            logging.error("Parameter space must be 'pm+parallax' or 'pm_only'")
            raise ValueError("Parameter space must be 'pm+parallax' or 'pm_only'")
    
    
    # Load data
    logging.info("Loading data...")
    X, Xerr, df = load_and_extract(
        input_file,
        data_columns=data_columns,
        errors_columns=errors_columns,
    )
    
    
    # Load GMM parameters
    logging.info(f"Loading GMM parameters from {gmm_params_dir}")
    mean, cov, weights = load_mcw_arrays_from_input_dir(gmm_params_dir)
    mcw_memb = (mean[-1], cov[-1], np.array([1.0]))
    mcw_field = (mean[:-1], cov[:-1], weights[:-1] / np.sum(weights[:-1]))
    
    # Calcular por lotes
    logging.info("Computing likelihoods...")
    
    pdf_memb = np.zeros(X.shape[0])
    pdf_field = np.zeros(X.shape[0])
    
    batch_size = bs
    num_batches = X.shape[0] // batch_size + (1 if X.shape[0] % batch_size != 0 else 0)
    logging.info(f"{num_batches=}")
    
    for i in range(num_batches):
        print(i+1, num_batches)
        logging.info(f"iteration: {i}/{num_batches}")
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, X.shape[0])
        X_batch = X[start_idx:end_idx]
        Xerr_batch = Xerr[start_idx:end_idx]
        pdf_memb_batch, pdf_field_batch = get_field_and_memb_likelihoods(
            X_batch, Xerr_batch, mcw_memb, mcw_field
        )
        pdf_memb[start_idx:end_idx] = pdf_memb_batch
        pdf_field[start_idx:end_idx] = pdf_field_batch
    
    
    df["prob_xi_memb"] = pdf_memb
    df["prob_xi_field"] = pdf_field
    
    
    if prob:
        logging.info("Computing total...")
        q_memb, q_field = get_probability(
            prob_xi_memb=pdf_memb,
            prob_xi_field=pdf_field,
            eta_0=0.01,
            iterations=1
        )
        df["q_memb"] = q_memb
        df["q_field"] = q_field
    
    
    logging.info("Saving results...")
    save_as_fits(output_file, df)


if __name__ == "__main__":
    main()

