#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

dt = np.dtype(('u4', [('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')]))
complex_dt = np.dtype(('i4', {'complex': ('i2', 0), 'imag': ('i2', 2)}))
array_2 = np.array([], complex_dt)
array = np.array([155, 255, 80, 0], dt)
array['r'] = 155
print(array_2['imag'])
