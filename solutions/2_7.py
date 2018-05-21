import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

def coin(x):
	return 2*np.random.randint(2,size=x)-1

simlen = 100000
X=coin(simlen)
N=np.random.normal(0,1,simlen)
A=np.linspace(0,4,30)
y_axis=[]
for i in range(0,30):
	Y=A[i]*X+N
	#errX = np.nonzero(X==1)
	errY = np.nonzero(-N>A[i])
	p_err = np.size(errY)/simlen
	#p_errX = np.size(errX)/simlen
	y_axis.append(p_err)


plt.plot(A,scipy.special.erfc(A/np.sqrt(2))/2,'ro')
plt.plot(A,y_axis,'go')
plt.xlabel('$A$')
plt.ylabel('$P_A()$')
plt.show()