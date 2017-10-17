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


def line_function(x, slope=0.7, intercept=0.1):
    return slope * x + intercept


y_noise_level = 0.2
x_noise_level = 0.05
size = 50

x = np.random.rand(size)
y_no_noise = line_function(x)

# make vectors of noise with normal distributions
# these have standard deviation of the noise level above
y_noise = np.random.normal(scale=y_noise_level, size=size)
x_noise = np.random.normal(scale=x_noise_level, size=size)

# We are actually going to rescale these errors once more so that we can provide a "measurement precision" for each point. This looks strange, but it lets us have both a varying precision and errors within that precision.
x_precision = np.random.uniform(0.0, 1.0, size)
y_precision = np.random.uniform(0.0, 1.0, size)

# Now we scale the noise by this amount
x_noise *= x_precision
y_noise *= y_precision

# This scales the precision vector to be the standard deviation of the distribution from which the noise value was drawn
x_precision *= x_noise_level
y_precision *= y_noise_level

y_noisy = y_no_noise + y_noise
x_noisy = x + x_noise

with open('../data/data_nonoise.txt', 'w') as fout:
    for xi, yi in zip(x, y_no_noise):
        fout.write('{:f} {:f}\n'.format(xi, yi))

with open('../data/data.txt', 'w') as fout:
    for xi, yi, xp, yp in zip(x_noisy, y_noisy, x_precision, y_precision):
        fout.write('{:f} {:f} {:f} {:f}\n'.format(xi, yi, xp, yp))
