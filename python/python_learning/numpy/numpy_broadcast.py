#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
    NumPy 广播(Broadcast)
"""

__author__ = 'JKong'

import numpy as np

# 1. 维度相同 => 对应列相乘
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)

# 2. 维度不同，列相同
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([1, 2, 3])
print(a + b)
print(a * b)
