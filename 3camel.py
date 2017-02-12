# -*- coding: utf-8 -*-
from scipy.ndimage import imread
import numpy as np
import matplotlib.pyplot as plt

maxprice = 88.90
minprice = 37.99

import time

start_time = '05.05.2011 12:00:00'
stop_time = '12.02.2017 12:00:00'
pattern = '%d.%m.%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(start_time, pattern)))
print(epoch)
epoch = int(time.mktime(time.strptime(stop_time, pattern)))
print(epoch)

chart = imread(
    "C:/Users/franc/Downloads/camelchart-locale-frasin-b00ql1u4topricetypes-amazonforce-1zero-0w-2725h-1440desired-falselegend-0ilt-0fo-0lang-en2017-02-1200-43-36.png",
    flatten=False, mode=None)
raster = (chart.dot([2, 3, 5]) == (99 * 2 + 168 * 3 + 94 * 5))[-1::-2, ::2]
raster = np.array([np.nan, 1])[raster.astype(np.int)]
raster *= np.arange(raster.shape[0])[:, np.newaxis]
mymin = np.nanmin(raster, axis=0)
mymax = np.nanmax(raster, axis=0)
toto = np.vstack((mymax, mymin)).ravel("F")

toto -= np.nanmin(toto)
toto /= np.nanmax(toto)
toto *= maxprice - minprice
toto += minprice

plt.plot(toto)
