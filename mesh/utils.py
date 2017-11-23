# Copyright (c) 2017 Max Planck Society. All rights reserved.
# see accompanying LICENSE.txt file for licensing and contact information


def row(A):
    return A.reshape((1, -1))


def col(A):
    return A.reshape((-1, 1))


def sparse(i, j, data, m=None, n=None):
    import numpy as np
    from scipy.sparse import csc_matrix
    ij = np.vstack((i.flatten().reshape(1, -1), j.flatten().reshape(1, -1)))

    if m is None:
        return csc_matrix((data, ij))
    else:
        return csc_matrix((data, ij), shape=(m, n))
