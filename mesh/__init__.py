# Copyright (c) 2017 Max Planck Society. All rights reserved.
# see accompanying LICENSE.txt file for licensing and contact information


import os
from os.path import abspath, dirname, expanduser, join

from .mesh import Mesh
from .meshviewer import MeshViewer, MeshViewers

texture_path = abspath(join(dirname(__file__), '..', 'data', 'template', 'texture_coordinates'))

if 'PSBODY_MESH_CACHE' in os.environ:
    mesh_package_cache_folder = expanduser(os.environ['PSBODY_MESH_CACHE'])
else:
    mesh_package_cache_folder = expanduser('~/.psbody/meshlite_package_cache')

if not os.path.exists(mesh_package_cache_folder):
    os.makedirs(mesh_package_cache_folder)
