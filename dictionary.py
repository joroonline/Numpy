#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from sys import getsizeof


dt = np.dtype(('u4', [('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')]))
complex_dt = np.dtype(('i4', {'complex': ('i2', 0), 'imag': ('i2', 2)}))
array_2 = np.array([], complex_dt)
array = np.array([155, 255, 80, 0], dt)
dic = {'red': 255, 'green': 255, 'blue': 255, 'alpha': 255}
print(array_2['imag'])
print(f"Size of python List: {getsizeof(dic) / 1000000}MB")
print(f"Size of numpy array: {getsizeof(array) / 1000000}MB")
print(f"Numpy use {getsizeof(dic)/getsizeof(array)} less memory")
