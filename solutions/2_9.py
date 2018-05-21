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
l=np.linspace(0,8,60)
A=4
y_axis=[]
for i in range(0,60):
	Y=A*X+N
	#errX = np.nonzero(X==1)
	err1 = np.nonzero(N<-A+l[i])
	p_err = 2*np.size(err1)/simlen
	err2 = np.nonzero(N>A+l[i])
	p_err2 = 2*np.size(err2)/simlen
	#p_errX = np.size(errX)/simlen
	y_axis.append((p_err+p_err2)/2)


plt.plot(l,y_axis)

plt.xlabel('$lambda$')
plt.ylabel('$P_A()$')
plt.show()