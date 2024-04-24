import numpy as np
from scipy import linalg
import numpy.typing as npt


"""
Funcions borrowed from the astroML library.
"""


def log_multivariate_gaussian(x, mu, V, Vinv=None, method=1):
    """Evaluate a multivariate gaussian N(x|mu, V)

    This allows for multiple evaluations at once, using array broadcasting

    Parameters
    ----------
    x: array_like
        points, shape[-1] = n_features

    mu: array_like
        centers, shape[-1] = n_features

    V: array_like
        covariances, shape[-2:] = (n_features, n_features)

    Vinv: array_like or None
        pre-computed inverses of V: should have the same shape as V

    method: integer, optional
        method = 0: use cholesky decompositions of V
        method = 1: use explicit inverse of V

    Returns
    -------
    values: ndarray
        shape = broadcast(x.shape[:-1], mu.shape[:-1], V.shape[:-2])

    Examples
    --------

    >>> x = [1, 2]
    >>> mu = [0, 0]
    >>> V = [[2, 1], [1, 2]]
    >>> log_multivariate_gaussian(x, mu, V)
    -3.3871832107434003
    """
    x = np.asarray(x, dtype=float)
    mu = np.asarray(mu, dtype=float)
    V = np.asarray(V, dtype=float)

    ndim = x.shape[-1]
    x_mu = x - mu

    if V.shape[-2:] != (ndim, ndim):
        raise ValueError("Shape of (x-mu) and V do not match")

    Vshape = V.shape
    V = V.reshape([-1, ndim, ndim])

    if Vinv is not None:
        assert Vinv.shape == Vshape
        method = 1

    if method == 0:
        Vchol = np.array([linalg.cholesky(V[i], lower=True) for i in range(V.shape[0])])

        # we may be more efficient by using scipy.linalg.solve_triangular
        # with each cholesky decomposition
        VcholI = np.array([linalg.inv(Vchol[i]) for i in range(V.shape[0])])
        logdet = np.array(
            [2 * np.sum(np.log(np.diagonal(Vchol[i]))) for i in range(V.shape[0])]
        )

        VcholI = VcholI.reshape(Vshape)
        logdet = logdet.reshape(Vshape[:-2])

        VcIx = np.sum(
            VcholI * x_mu.reshape(x_mu.shape[:-1] + (1,) + x_mu.shape[-1:]), -1
        )
        xVIx = np.sum(VcIx**2, -1)

    elif method == 1:
        if Vinv is None:
            Vinv = np.array([linalg.inv(V[i]) for i in range(V.shape[0])]).reshape(
                Vshape
            )
        else:
            assert Vinv.shape == Vshape

        logdet = np.log(np.array([linalg.det(V[i]) for i in range(V.shape[0])]))
        logdet = logdet.reshape(Vshape[:-2])

        xVI = np.sum(x_mu.reshape(x_mu.shape + (1,)) * Vinv, -2)
        xVIx = np.sum(xVI * x_mu, -1)

    else:
        raise ValueError(f"unrecognized method {method}")

    return -0.5 * ndim * np.log(2 * np.pi) - 0.5 * (logdet + xVIx)


def gmm_pdf(X, Xerr, V, mu, alpha):
    """
    Evaluate the probability for a set of points

    Parameters
    ----------
    X: array_like
        Input data. shape = (n_samples, n_features)
    Xerr: array_like
        Error on input data.  shape = (n_samples, n_features, n_features)

    Returns
    -------
    p: ndarray
        Probabilities.  shape = (n_samples,)
    """
    X = np.asarray(X)
    Xerr = np.asarray(Xerr)
    n_samples, n_features = X.shape

    # assume full covariances of data
    assert Xerr.shape == (n_samples, n_features, n_features)

    X = X[:, np.newaxis, :]
    Xerr = Xerr[:, np.newaxis, :, :]
    T = Xerr + V

    return np.sum(np.exp(log_multivariate_gaussian(X, mu, T) + np.log(alpha)), axis=-1)


def get_correlation_matrix_3x3(
    dx: npt.NDArray, dy: npt.NDArray, dz: npt.NDArray, X: npt.NDArray
):
    """
    Construct the correlation matrix for the proper motions.

    Parameters
    ----------
    dx : array_like
        The proper motion error in the ra direction.
    dy : array_like
        The proper motion error in the dec direction.
    dz : array_like
        The parallax error.
    X : array_like
        The proper motions.
    """
    Xerr = np.zeros(X.shape + X.shape[-1:])
    diag = np.arange(X.shape[-1])
    Xerr[:, diag, diag] = np.vstack([dx**2, dy**2, dz**2]).T
    return Xerr


def get_correlation_matrix_2x2(dx: npt.NDArray, dy: npt.NDArray, X: npt.NDArray):
    """
    Construct the correlation matrix for the proper motions.

    Parameters
    ----------
    dx : array_like
        The proper motion error in the ra direction.
    dy : array_like
        The proper motion error in the dec direction.
    X : array_like
        The proper motions.
    """
    Xerr = np.zeros(X.shape + X.shape[-1:])
    diag = np.arange(X.shape[-1])
    Xerr[:, diag, diag] = np.vstack([dx**2, dy**2]).T
    return Xerr
