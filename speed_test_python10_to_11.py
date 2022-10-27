#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
from sys import getsizeof
from timeit import Timer


def python():
    res = [X[i] * Y[i] for i in range(len(X))]
    return res

def numpy():
    res = np_X * np_Y
    return res

def comparison_storage():
    print(f"Size of python List: {getsizeof(X) / 1000000}MB")
    print(f"Size of numpy array: {getsizeof(np_X) / 1000000}MB")

def comparison_time():
    print(f"Time for Python was : {time_python}")
    print(f"Time for Numpy was : {time_numpy}")


sz = 1000000

X = [random.randint(0, 200) for _ in range(sz)]
Y = [random.randint(0, 200) for _ in range(sz)]
np_X = np.array(X)
np_Y = np.array(Y)

time_python = Timer("python()", "from __main__ import python").timeit(10)
time_numpy = Timer("numpy()", "from __main__ import numpy").timeit(10)
comparison_storage()
comparison_time()
print(f"Numpy was {time_python / time_numpy} times faster and use {getsizeof(X) / getsizeof(np_X)} "
      f"times less memory.")

# Python 3.10
# Numpy with dtype is 279 times faster than as python 3.10
# Numpy without dtype is 74 times faster than as python

# Python 3.11
# Numpy with dtype is 172 times faster than as python 3.11 -> 38%
# Numpy without dtype is 36 times faster than python 3.11 -> 51%
