import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

maxrange =50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)
simlen = 100000
err=[]
pdf=[]
h=2*maxlim/(maxrange-1)

for j in range(0,10):
	mu=np.random.normal(0,10)
	sigma=np.square(np.random.normal(0,10))
	n = np.random.normal(mu,sigma,simlen)
	for i in range(0,maxrange):
		err_ind = np.nonzero(n<x[i])
		err_n = np.size(err_ind)
		err.append(err_n/simlen);
	for i in range(0,maxrange-1):
		test = (err[i+1]-err[i])/(x[i+1]-x[i])
		pdf.append(test)
	def gauss_pdf(x):
		return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-x**2/2.0)
	vec_gauss_pdf = scipy.vectorize(gauss_pdf)

	# plt.plot(x[0:(maxrange-1)].T,pdf,'o')
	plt.plot(x,vec_gauss_pdf(x))


plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.show()





