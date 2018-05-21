#!/usr/bin/env python

#this program generates a gaussian random no wirh 0 mean and unit variance

import numpy as np
import mpmath as mp
import scipy 
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

simlen = 100000 
x = np.linspace(-4,4,30)
n = np.random.normal(0,1,simlen)
err = []

for i in range(0,30):
	err_ind = np.nonzero(n<x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

plt.plot(x.T,err)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()




