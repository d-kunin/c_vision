__author__ = '7times6'

from PIL import Image
import numpy as np


def pca(X):
    # get dimensions
    num_data, dim = X.shape

    # center data
    mean_X = X.mean(axis=0)
    X = X - mean_X # X is centered now

    if dim > num_data:
        # PCA compact trick
        M = np.dot(X, X.T)  # covariance matrix
        e, EV = np.linalg.eig(M)  # eigenvalues and vectors
        tmp = np.dot(X.T, EV).T # compact trick?
        V = tmp[::-1]  # reverse
        S = np.sqrt(e)[::-1] # reverse
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        # PCA - SVD
        U,S,V = np.linalg.svd(X)
        V = V[:num_data]  # only this data have sense

    return V, S, mean_X