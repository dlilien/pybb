#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 dlilien <dlilien90@gmail.com>
#
# Distributed under terms of the MIT license.

"""
This is an example of how to create a class. We'll do something useful!
"""

import numpy as np
import matplotlib.pyplot as plt
import gdal


class RasterDataset():
    
    def __init__(self, fn=None):
        """
        This is called when we create this object

        Here I just set some blank attributes so the user knows what this will have, unless you pass a filename then we do the loading

        Parameters
        ----------
        fn: str, optional
            The file to load. Default is an empty dataset.

        Attributes
        ----------
        x: np.ndarray
            x coordinates
        y: np.ndarray
            y coordinates
        data: np.ndarray
            The raster data
        gt: tuple
            The geometric transform of the data (see gdal docs)
        projection: str
            The projection type (e.g. wgs84)
        """
        if fn is not None:
            self.load_file(fn)
        else:
            self.x = None
            self.y = None
            self.data = None
            self.gt = None
            self.projection = None

    def _load_ds(self, ds, dtype=np.float64, ndv=-9999):  # this method is intended to be called only by the author of this class, as signaled by the leading underscore
        self.data = np.array(ds.GetRasterBand(1).ReadAsArray(), dtype=dtype)
        if ndv is not None:
            self.data[self.data == ndv] = np.nan
        len_y, len_x = self.data.shape
        self.gt = ds.GetGeoTransform()
        x0 = self.gt[0]
        y0 = self.gt[3]
        xM = self.gt[1] * len_x + x0
        yM = self.gt[5] * len_y + y0
        self.x = np.linspace(x0, xM, len_x)
        self.y = np.linspace(y0, yM, len_y)
        self.projection = ds.GetProjectionRef() 

    def load_file(self, fn, dtype=np.float64, ndv=-9999):
        ds = gdal.Open(fn)
        self._load_ds(ds, dtype=dtype, ndv=ndv)

    def really_cool_feature(self, *arg, **kwargs):
        pass  # This lets me create a framework that is not yet implemented

    def contourf(self, ax=None, nlevels=256, vmin=None, vmax=None, **kwargs):
        if ax is None:
            fig, ax = plt.subplots()
        if vmin is None:
            vmin = np.min(self.data)
        if vmax is None:
            vmax = np.max(self.data)

        return ax.contourf(self.x, self.y, self.data, np.linspace(vmin, vmax, num=nlevels), **kwargs)
