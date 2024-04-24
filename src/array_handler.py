from pathlib import Path
import re

import numpy as np
import numpy.typing as npt

"""
This module contains functions to save and load mean, covariance and weights arrays to and from .npy and text files.
"""

MCW_arrays = tuple[npt.NDArray, npt.NDArray, npt.NDArray]


def _save_mcw_arrays_to_npy_file(arrays: MCW_arrays, output_file: str | Path) -> None:
    """Save a list of arrays representing mean, covariance and weights to a .npy file."""
    with open(output_file, "wb") as f:
        for array in arrays:
            np.save(f, array)


def _read_npy_file_to_mcw_arrays(input_file: str | Path) -> MCW_arrays:
    """Read a list of arrays representing mean, covariance and weights from a .npy file."""
    arrays = []
    with open(input_file, "rb") as f:
        for _ in range(3):
            arrays.append(np.load(f))
    return tuple(arrays)


def _array3d_to_text_file(output_file: str | Path, array_data: npt.NDArray) -> None:
    """
    Save a 3D array to a text file.
    Ref: https://stackoverflow.com/questions/15746954/what-is-the-difference-between-rb-and-rb-modes-in-file-objects
    """
    with open(output_file, "w") as f:
        f.write(f"# Shape: {array_data.shape}\n")
        for array_slice in array_data:
            np.savetxt(f, array_slice)
            f.write("# New slice\n")


def _text_file_to_array3d(input_file: str | Path) -> npt.NDArray:
    """
    Read a 3D array from a text file.
    """

    with open(input_file, "r") as f:

        # Extract the dimensions of the array
        shape_string = f.readline()
        match = re.search(r"\((\d+,?\s?)+\)", shape_string)

        if match:
            shape_string = match.group(0)
            shape = tuple(map(int, shape_string.strip("()").split(",")))
        else:
            raise ValueError("Invalid shape string")

    return np.loadtxt(input_file).reshape(shape)


def load_mcw_arrays_from_text_files(
    mean_file: str | Path, cov_file: str | Path, weights_file: str | Path
) -> MCW_arrays:
    """Load mean, covariance and weights from text files."""
    
    mean = np.loadtxt(mean_file)
    cov = _text_file_to_array3d(cov_file)
    weights = np.loadtxt(weights_file)
    
    return mean, cov, weights  #  {"mean": mean, "cov": cov, "weights": weights}


def load_mcw_arrays_from_input_dir(input_dir: str | Path) -> MCW_arrays:
    """Load mean, covariance and weights from text files in an input directory."""
    
    input_dir = Path(input_dir)
    mean_file = input_dir / "mean.txt"
    cov_file = input_dir / "cov.txt"
    weights_file = input_dir / "weights.txt"
    
    if not mean_file.exists() or not cov_file.exists() or not weights_file.exists():
        raise FileNotFoundError("GMM parameters files do not exist") 
    
    return load_mcw_arrays_from_text_files(mean_file, cov_file, weights_file)


if __name__ == "__main__":

    print("This is array_handler.py module.")

    MEAN = np.array(
        [
            [-1.48652764, -7.01608699, 0.10714429],
            [-2.21556396, -6.07484421, 0.09800103],
            [-2.8201513, -5.76041052, 0.09320752],
            [-0.56466291, -2.04877037, 0.21940266],
            [-4.54496915, -5.12095505, 0.10836441],
            [-0.34895071, -3.41719793, 0.11645846],
            [-2.69501248, -1.3498241, 0.01618732],  # THIS!!!!
        ]
    )

    COV = np.array(
        [
            [
                [4.54036089e00, 1.28219910e00, 4.38616262e-03],
                [1.28219910e00, 3.60279212e00, 3.45312145e-03],
                [4.38616262e-03, 3.45312145e-03, 5.18802026e-04],
            ],
            [
                [1.80146070e01, 1.92436702e00, 3.88270649e-02],
                [1.92436702e00, 1.73228381e01, -3.56890662e-02],
                [3.88270649e-02, -3.56890662e-02, 1.91323089e-02],
            ],
            [
                [2.63107531e00, 5.90524102e-01, 8.83918733e-03],
                [5.90524102e-01, 2.89774762e00, 1.30275773e-02],
                [8.83918733e-03, 1.30275773e-02, 2.27950766e-03],
            ],
            [
                [5.24841135e00, 6.73093176e-01, 3.11190196e-02],
                [6.73093176e-01, 5.21616024e00, 1.65340384e-02],
                [3.11190196e-02, 1.65340384e-02, 3.05610664e-03],
            ],
            [
                [3.38272326e00, 3.17713879e-01, 1.65662357e-03],
                [3.17713879e-01, 4.42339144e00, 7.19861254e-03],
                [1.65662357e-03, 7.19861254e-03, 5.62481637e-04],
            ],
            [
                [3.18765543e00, -8.78984184e-01, -2.50823890e-03],
                [-8.78984184e-01, 4.34527279e00, 5.38698868e-03],
                [-2.50823890e-03, 5.38698868e-03, 5.71385078e-04],
            ],
            [
                [2.18459931e-02, 5.93310620e-03, -6.29362304e-04],
                [5.93310620e-03, 1.94960168e-02, 1.23035051e-04],
                [-6.29362304e-04, 1.23035051e-04, 8.67501316e-04],
            ],
        ]
    )

    W = [
        0.17322741,
        0.04779954,
        0.2680493,
        0.0842031,
        0.24263252,
        0.17570589,
        0.00838224,
    ]

    data_dir = Path("gmm_params/pm+par_7comp/")
    mean_file = data_dir / "mean.txt"
    cov_file = data_dir / "cov.txt"
    weights_file = data_dir / "weights.txt"

    np.savetxt(
        mean_file,
        MEAN,
    )
    _array3d_to_text_file(cov_file, COV)
    np.savetxt(weights_file, W)
