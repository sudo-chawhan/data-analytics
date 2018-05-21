import numpy as np
import scipy 
from mpl_toolkits.mplot3d import Axes3D
import mpmath as mp
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

simlen=1000000
x=np.linspace(0,1,50)
filename = "uni3.txt"
file = open(filename, "r")
temp = [float(line[:-1]) for line in file]
ran=np.asarray(temp)
err=[]
for i in range(0,50):
	err_ind = np.nonzero(ran<x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

plt.plot(x,err)
plt.show()