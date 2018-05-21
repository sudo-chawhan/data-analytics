import numpy as np
import scipy 
import mpmath as mp
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
simlen=int(1e5)
X1 = np.random.normal(0,1,simlen)
X2 = np.random.normal(0,1,simlen)
N=np.random.normal(0,1,simlen)
A = np.sqrt(np.square(X1)+np.square(X2))
gamma=np.linspace(1,10,20)
err=[]
err2=[]
for i in range(0,20):
	err.append(0.5*(1-np.sqrt(gamma[i]/(2+gamma[i]))))
for i in range(0,20):
	Y=(np.sqrt(gamma[i]/2)*A)+N
	err_a=np.nonzero(Y<0)
	err_size=np.size(err_a)/simlen
	err2.append(err_size)
plt.semilogy(gamma,err,"g")
plt.semilogy(gamma,err2,"ro")
plt.plot()
plt.show()