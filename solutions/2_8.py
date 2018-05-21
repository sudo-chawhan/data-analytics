import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess


simlen = 100000
X=1
N=np.random.normal(0,1,simlen)
A=np.linspace(1,np.sqrt(10),30)
y_axis=[]
for i in range(0,30):
	Y=A[i]*X+N
	errY = np.nonzero(-N>A[i])
	p_err = np.size(errY)/simlen
	y_axis.append(p_err)

plt.plot(A,y_axis,'go')
plt.plot(A,scipy.special.erfc(A/np.sqrt(2))/2,'r')

plt.xlabel('$snr$')
plt.ylabel('$P_A()$')
plt.show()