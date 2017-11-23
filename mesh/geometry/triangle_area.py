# Copyright (c) 2017 Max Planck Society. All rights reserved.
# see accompanying LICENSE.txt file for licensing and contact information


from .tri_normals import TriToScaledNormal
import numpy as np


def triangle_area(v, f):
    """Computes the area associated to a set of triangles"""
    return (np.sqrt(np.sum(TriToScaledNormal(v, f) ** 2, axis=1)) / 2.).flatten()
