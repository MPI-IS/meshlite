# (c) 2015-2016 Max Planck Society
# see accompanying LICENSE.txt file for licensing and contact information

try:
    # setuptools is required
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext
    from setuptools.command.install import install
    has_setup_tools = True
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.install import install
    from distutils.command.build_ext import build_ext
    has_setup_tools = False

from distutils.util import convert_path
from distutils import log
from distutils.command.sdist import sdist
import os

# this package will go to the following namespace
namespace_package = 'psbody'


def _get_version():
    """Convenient function returning the version of this package"""

    ns = {}
    version_path = convert_path('mesh/version.py')
    if not os.path.exists(version_path):
        return None
    with open(version_path) as version_file:
        exec(version_file.read(), ns)

    log.warn('[VERSION] read version is %s', ns['__version__'])
    return ns['__version__']


def _get_all_extensions():
    try:
        import numpy
    except:
        return []

    # valid only for gcc/clang
    extra_args = ['-O3']

    import sys
    if sys.platform.find('linux') > -1:
        extra_args += ['-fopenmp']  # openmp not supported on OSX

    define_macros = [('NDEBUG', '1')]
    undef_macros = []
    package_name_and_srcs = [('serialization.plyutils', ['mesh/src/plyutils.c', 'mesh/src/rply.c'], []),
                             ('serialization.loadobj', ['mesh/src/py_loadobj.cpp'], []),
                             ]

    out = []
    for current_package_name, src_list, additional_defines in package_name_and_srcs:
        ext = Extension("%s.meshlite.%s" % (namespace_package, current_package_name),
                         src_list,
                         language="c++",
                         include_dirs=['mesh/src', numpy.get_include()],
                         libraries=[],
                         define_macros=define_macros + additional_defines,
                         undef_macros=undef_macros,
                         extra_compile_args=extra_args,
                         extra_link_args=extra_args)

        out += [ext]
    return out

all_extensions = _get_all_extensions()

additional_kwargs = {}
if has_setup_tools:
    # setup tools required for the 'setup_requires' ...
    additional_kwargs['setup_requires'] = ['setuptools', 'numpy']
    additional_kwargs['install_requires'] = ['numpy >= 1.8', 'scipy', 'pyopengl', 'pyzmq']
    additional_kwargs['zip_safe'] = not all_extensions
    additional_kwargs['test_suite'] = "tests"
    additional_kwargs['namespace_packages'] = [namespace_package]

cmdclass = {'build_ext': build_ext,
            'sdist': sdist,
            'install': install}

# check if the namespace  works for python >= 3.3
packages = [namespace_package,
            '%s.meshlite' % namespace_package,
            '%s.meshlite.geometry' % namespace_package,
            '%s.meshlite.serialization' % namespace_package
            ]  # actual subpackage described here

package_dir = {namespace_package: '%s-meshlite-namespace' % namespace_package,
               '%s.meshlite' % namespace_package: 'mesh',  # actual subpackage described here
               '%s.meshlite.geometry' % namespace_package: 'mesh/geometry',
               '%s.meshlite.serialization' % namespace_package: 'mesh/serialization',
               }

setup(name='%s-meshlite' % namespace_package,
      version=_get_version(),
      packages=packages,
      package_dir=package_dir,
      ext_modules=all_extensions,
      author='Max Planck Perceiving Systems - Body Group',
      maintainer='Naureen Mahmood',
      maintainer_email='naureen.mahmood@tuebingen.mpg.de',
      url='http://ps.is.tuebingen.mpg.de',
      description='Mesh and MeshViewer utilities',
      license='Unlicensed',
      cmdclass=cmdclass,
      ** additional_kwargs
      )
