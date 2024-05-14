import numpy as np
import numpy.typing as npt
import logging

from src.stats import get_correlation_matrix_3x3, gmm_pdf, get_correlation_matrix_2x2


def get_field_and_memb_likelihoods(
    X: npt.NDArray,
    Xerr: npt.NDArray,
    mcw_memb: tuple[npt.NDArray, npt.NDArray, npt.NDArray],
    mcw_field: tuple[npt.NDArray, npt.NDArray, npt.NDArray],
) -> tuple[npt.NDArray, npt.NDArray]:
    """
    Compute the likelihoods based on the data and the XDGMMs obtained
    """

    # Check arrays has the same dimension
    if X.shape != Xerr.shape:
        raise ValueError("X and Xerr arrays must have the same shape")

    n_dim = X.shape[1]
    if n_dim == 3:
        Xerr_ = get_correlation_matrix_3x3(Xerr[:, 0], Xerr[:, 1], Xerr[:, 2], X)
    elif n_dim == 2:
        Xerr_ = get_correlation_matrix_2x2(Xerr[:, 0], Xerr[:, 1], X)
    else:
        raise ValueError("Only 2D and 3D data is supported")

    pdf_field = gmm_pdf(X, Xerr_, mu=mcw_field[0], V=mcw_field[1], alpha=mcw_field[2])
    pdf_memb = gmm_pdf(X, Xerr_, mu=mcw_memb[0], V=mcw_memb[1], alpha=mcw_memb[2])

    return pdf_memb, pdf_field


def get_probability(
    prob_xi_memb: npt.NDArray,
    prob_xi_field: npt.NDArray,
    eta_0=0.01,
    iterations=1,
) -> tuple[npt.NDArray, npt.NDArray]:
    """Get the probability of being a member based on the likelihoods

    Args:
        prob_xi_memb (npt.NDArray): pdf_memb
        prob_xi_field (npt.NDArray): pdf_field
        eta_0 (float, optional): Initial fraction of members. Defaults to 0.01.
        iterations (int, optional): Number of iterations to determine eta. Defaults to 1.

    Returns:
        npt.NDArray: probabilities of being a member
    """
    eta = eta_0
    for i in range(iterations):
        total_likelihood = eta * prob_xi_memb + (1 - eta) * prob_xi_field
        q_memb_i = eta * prob_xi_memb / total_likelihood
        q_field_i = (1 - eta) * prob_xi_field / total_likelihood
        mask = np.isnan(q_memb_i)
        eta = np.average(q_memb_i[~mask])
        logging.info(f"Iteration {i+1}: eta = {eta}")

    return q_memb_i, q_field_i
