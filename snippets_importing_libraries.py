# -*- coding: utf-8 -*-
"""Snippets: Importing libraries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bYFGLyptbhX3jZ535FX-qGfr60NEhdEM
"""

!pip install matplotlib-venn

!apt-get -qq install -y libfluidsynth1

# https://pypi.python.org/pypi/libarchive
!apt-get -qq install -y libarchive-dev && pip install -U libarchive
import libarchive

# https://pypi.python.org/pypi/pydot
!apt-get -qq install -y graphviz && pip install pydot
import pydot

!pip install cartopy
import cartopy