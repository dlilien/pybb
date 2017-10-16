#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 dlilien <dlilien@berens>
#
# Distributed under terms of the MIT license.

"""
This will make a text file with data that we will read to linearly regress
"""

import numpy as np


def line_function(x):
    return 0.7 * x + 0.1


noise_level = 0.2
size = 100

x = np.random.rand(size)
y_no_noise = line_function(x)
noise = np.random.normal(scale=noise_level, size=size)
y_noise = y_no_noise + noise

with open('data.txt', 'w') as fout:
    for xi, ynni, yni in zip(x, y_no_noise, y_noise):
        fout.write('{:f} {:f} {:f}\n'.format(xi, ynni, yni))
