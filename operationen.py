#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


x = np.array([
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ],
    ])

y = np.array([
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ],
    ])


print(np.dot(x, y))