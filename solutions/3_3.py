import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

simlen=100000
X1 = np.random.normal(0,1,simlen)
X2 = np.random.normal(0,1,simlen)

V =np.square(X1) + np.square(X2)


# def gauss_pdf(x):
# 	return 1/np.sqrt(2*np.pi)∗ np.exp(−x**2/2.0)

# def gauss_pdf_sum(x1,x2):
# 	return 

err = []
pdf = []
x = np.linspace(-1,4,30)
for i in range(0,30):
	err_ind = np.nonzero(V<x[i])
	err_n = np.size(err_ind)
	err.append(err_n/simlen)

def quer(x):
	return (1-np.exp(-alpha*x))

for i in range(0,29):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test)

plt.plot(x,np.sqrt(err),"g")
plt.plot(x[0:29],np.sqrt(pdf),"r")
plt.xlabel("x")
plt.ylabel("V")
plt.legend(["cdf","pdf"])
plt.grid()
plt.show()