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
def main(f, o, p):

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

    # Load data
    logging.info("Loading data...")
    X, Xerr, df = load_and_extract(
        input_file,
        data_columns=["pmra", "pmra", "parallax"],
        errors_columns=["pmra_error", "pmra_error", "parallax_error"],
    )
    
    # Load GMM parameters
    logging.info("Loading GMM parameters")
    mean, cov, weights = load_mcw_arrays_from_input_dir(gmm_params_dir)
    mcw_memb = (mean[-1], cov[-1], np.array([1.0]))
    mcw_field = (mean[:-1], cov[:-1], weights[:-1]/np.sum(weights[:-1]))
    
    logging.info("Computing probabilities...")
    pdf_memb, pdf_field = get_field_and_memb_likelihoods(X, Xerr, mcw_memb, mcw_field)
    q_memb_i = get_probability(pdf_memb, pdf_field, eta_0 =0.01, iterations = 1)
    
    logging.info("Saving results...")
    df["prob_xi_memb"] = pdf_memb
    df["prob_xi_field"] = pdf_field
    df["q_memb_i"] = q_memb_i
    save_as_fits(output_file, df)
    

if __name__ == "__main__":
    main()