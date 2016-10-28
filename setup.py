#!/usr/bin/env python

import os
import sys
from setuptools import setup

from src import fslask

# Usaremos este archivo como descripcion de nuestro paquete
readme = os.path.join(os.path.dirname(sys.argv[0]), 'README.rst')

# Definir nuestro paquete para distribuir
setup(
    name=fslask.__name__,  # nuestro nombre
    packages=[
        'fslask',   # solo tenemos 1 paquete por el momento
    ],
    package_dir={
        '': 'src',  # donde vive el codigo fuente
    },
    version=fslask.__version__,  # reusamos la version en nuestro paquete
    url='https://github.com/thekad/FSLask',  # donde vive nuestro codigo fuente
    description=fslask.__desc__,  # reusamos la descripcion de nuestro paquete
    author='Jorge Gallegos',  # autor
    author_email='kad@blegh.net',  # email del autor
    license='MIT',  # licencia
    long_description=open(readme).read(),
    entry_points={
        'console_scripts': [
            'fslask-server=fslask.server:main',
        ],
    },
)
