#! /bin/usr/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random


array = [random.randint(0, 100) for _ in range(100)]
np_array = np.array([
    [
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)]
    ],
    [
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)]
    ],
    [
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)]
    ],
    [
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)],
        [random.randint(0, 100) for _ in range(100)]
    ]])

culums = np.array(
    [
        [0, 0], [0, 2]
    ], dtype=np.intp)
rows = np.array(
    [
        [2, 2], [2, 2]
    ], dtype=np.intp)

print(np_array)
print(np_array[rows, culums])
