from pathlib import Path

from astropy.table import Table
import numpy.typing as npt
import pandas as pd


def load_and_extract(
    input_file: str | Path, data_columns: list[str], errors_columns: list[str]
) -> tuple[npt.NDArray, npt.NDArray, pd.DataFrame]:
    """
    Load the input file as a pandas DataFrame, process it
    and return the data and errors as numpy arrays.
    """
    if input_file.suffix == ".csv":
        df = pd.read_csv(input_file)
    elif input_file.suffix == ".fits":
        df = Table.read(input_file).to_pandas()
    else:
        raise ValueError("Invalid file format")

    # Remove rows with missing data
    all_cols = data_columns + errors_columns
    df = df.dropna(subset=all_cols)

    X = df[data_columns].to_numpy()
    errX = df[errors_columns].to_numpy()

    return X, errX, df


def save_as_fits(output_file: str | Path, df: pd.DataFrame) -> None:
    """Save the DataFrame to a fits file."""
    Table.from_pandas(df).write(output_file, overwrite=True)
