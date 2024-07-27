import os
# Avoid automatic extra parallelization by other modules
os.environ['OMP_NUM_THREADS'] = "1"
os.environ['OPENBLAS_NUM_THREADS'] = "1"
os.environ['MKL_NUM_THREADS'] = "1"
os.environ['VECLIB_MAXIMUM_THREADS'] = "1"
os.environ['NUMEXPR_NUM_THREADS'] = "1"


import click
from pathlib import Path

from astropy.table import Table


@click.command()
@click.option("-f", help="Input fits file", required=True)
@click.option("-o", help="Output fits file", required=True)
@click.option("-ks", help="Threshold Ks mag", type=float, default=16.0)
@click.option("-p", help="Threshold parallax", type=float, default=0.1)
def main(f, o, ks, p):
    
    input_file, output_file = Path(f), Path(o)
    
    if not input_file.exists():
        raise FileNotFoundError("Input file does not exist")
    
    if output_file.exists():
        raise FileExistsError("Output file already exists")
    
    t = Table.read(input_file, format="fits")
    mask_parallax = t["parallax"] <= p
    mask_magKs = t["mag_Ks"] <= ks
    t_cuts = t[mask_parallax & mask_magKs]
    t_cuts.write(output_file, format="fits")


if __name__ == "__main__":
    main()
