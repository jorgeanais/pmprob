import os
# Avoid automatic extra parallelization by other modules
os.environ['OMP_NUM_THREADS'] = "1"
os.environ['OPENBLAS_NUM_THREADS'] = "1"
os.environ['MKL_NUM_THREADS'] = "1"
os.environ['VECLIB_MAXIMUM_THREADS'] = "1"
os.environ['NUMEXPR_NUM_THREADS'] = "1"

import click
import logging
from pathlib import Path

from astropy.table import Table
import numpy as np
import pandas as pd

from src.array_handler import load_mcw_arrays_from_input_dir
from src.dataloader import load_and_extract, save_as_fits
from src.prob import get_field_and_memb_likelihoods, get_probability


@click.command()
@click.option("-f", help="Input fits file", required=True)
@click.option("-o", help="Output fits file", required=True)
@click.option("-eta", help="Initial eta value", type=float, default=0.01)
@click.option("-niter", help="Number of iterations", type=int, default=1)
def main(f, o, eta, niter):
    
    # Initialize logger
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logfile_totalprob.txt",
        level=logging.DEBUG,
    )
    logging.info("--Program Started: Total probabilities--")
    logging.info(f"Input file: {f}")
    logging.info(f"Output file: {o}")
    logging.info(f"Initial eta value: {eta}")
    logging.info(f"Number of iterations: {niter}")
    
    # Inputs
    input_file, output_file = Path(f), Path(o)
    
    if not input_file.exists():
        logging.error("Input file does not exist")
        raise FileNotFoundError("Input file does not exist")
    
    if output_file.exists():
        logging.error("Output file already exists")
        raise FileExistsError("Output file already exists")
    
    # Load data
    df = Table.read(input_file).to_pandas()
    
    logging.info("Read likelihoods...")
    pdf_memb = df["prob_xi_memb"]
    pdf_field = df["prob_xi_field"]
    
    # MAIN
    logging.info("Computing total probabilities...")
    q_memb, q_field = get_probability(
        prob_xi_memb=pdf_memb,
        prob_xi_field=pdf_field,
        eta_0=float(eta),
        iterations=int(niter),
    )
    df["q_memb"] = q_memb
    df["q_field"] = q_field
    
    
    logging.info("Saving results...")
    save_as_fits(output_file, df)


if __name__ == "__main__":
    main()
