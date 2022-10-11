#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import random
from timeit import Timer
from sys import getsizeof


def python():
    res = [X[i] * 2 for i in range(len(X))]
    return res


def numpy():
    res = np_X + np_Y
    return res


# create array in numpy
def array():
    temp = [-1.5, -1.2, 0.0, 2.1, 24.2]
    np_temp = np.array(temp)

    print(3 * np_temp)
    print([3 * x for x in temp])
    print(np.array([42, 1337, 127], np.int8))  # int8 -> 2^7-1 and int8 took 1 byte storage


# comparison from numpy array and python list
def comparison_storage():
    print(f"Size of python List: {getsizeof(X) / 1000000}MB")
    print(f"Size of numpy array: {getsizeof(np_X) / 1000000}MB")


def comparison_time():
    print(f"Time for Python was : {time_python}")
    print(f"Time for Numpy was : {time_numpy}")


if __name__ == '__main__':
    # create List and array for the comparison
    sz = 1000000

    dt = np.dtype(("i4", [("r", "u1"), ("g", "u1"), ("b", "u1"), ("a", "u1")]))  # -> u = unsigned integer  f = float
    arr = np.zeros((), dtype=dt)
    arr2 = {"r": 255, "g": 255, "b": 255, "a": 255}
    arr["r"] = 255
    arr["g"] = 128
    arr["b"] = 255
    arr["a"] = 255
    array = np.array([255, 128, 255, 255], dt)
    print(array["r"])
    print(arr.shape)

    X = [random.randint(0, 200) for _ in range(sz)]
    Y = [random.randint(0, 200) for _ in range(sz)]
    np_X = np.array(X, np.int16)
    np_Y = np.array(Y, np.int16)
    m = np.array(
        [
            [
                [random.randint(0, 20) for _ in range(10)],
                [random.randint(0, 20) for _ in range(10)],
                [random.randint(0, 20) for _ in range(10)]
            ],
            [
                [random.randint(0, 20) for _ in range(10)],
                [random.randint(0, 20) for _ in range(10)],
                [random.randint(0, 20) for _ in range(10)]
            ]
        ]
    )

    # variable for the time comparisoṇ̣
    time_python = Timer("python()", "from __main__ import python").timeit(10)
    time_numpy = Timer("numpy()", "from __main__ import numpy").timeit(10)

    # execute the comparison
    comparison_storage()
    comparison_time()
    print(f"Numpy was {time_python / time_numpy} times faster and use {getsizeof(X) / getsizeof(np_X)} "
          f"times less memory.")
