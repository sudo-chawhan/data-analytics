import numpy as np
import scipy 
from mpl_toolkits.mplot3d import Axes3D
import mpmath as mp
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

simlen=1000000
x=np.linspace(-10,10,50)
filename = "s.txt"
file = open(filename, "r")
temp = [float(line[:-1]) for line in file]
ran=np.asarray(temp)
err=[]
for i in range(0,50):
	err_ind = np.nonzero(ran<x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)
pdf=[]
for i in range(0,49):
	p=(err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(p)

sigma=np.linspace(0,1,10)
for i in range(0,10):
	px=(np.exp(-(x**2)/(2*np.square(sigma[i])))/(np.sqrt(2*np.pi)*sigma[i]))
	plt.plot(x,px)

plt.plot(x[0:49],pdf,"ro")
plt.show()