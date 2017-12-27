# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='coniii',
      version='0.1.0',
      description='CONvenient Interface to Inverse Ising',
      long_description=long_description,
      url='https://github.com/bcdaniels/coniii',
      author='Edward D. Lee, Bryan C Daniels',
      author_email='edl56@cornell.edu',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Researchers',
          'Topic :: Software Development :: Research Tools',
           'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
      #python_requires='==2.7',
      keywords='inverse ising maxent',
      packages=find_packages(),
      install_requires=['multiprocess','scipy','numpy','numba','dill'],
      package_data={'coniii':['custom_maxent.pyx','fast.pyx','setup_fast.py','__init__.py']},
      py_modules=['exact','generalModelRMC','ising','mc_hist','meanFieldIsing','pseudoInverseIsing','samplers','solvers','utils']
)
