# Copyright (c) 2017 Max Planck Society. All rights reserved.
# see accompanying LICENSE.txt file for licensing and contact information

"""
Error heirarchy for Mesh class
"""


class MeshError(Exception):
    """Base error class for Mesh-related errors"""
    pass


class SerializationError(MeshError):
    """Mesh reading or writing errors"""
    pass
