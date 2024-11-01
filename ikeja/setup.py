from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["los_cy.py"])
)

