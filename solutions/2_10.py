import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

def coin(x):
	return 2*np.random.randint(2,size=x)-1

def gauss(y,a):
	return (1/np.sqrt(2*np.pi))*(np.exp(-np.square(x-a)/2);


simlen = 100000
X=coin(simlen)
N=np.random.normal(0,1,simlen)
A=np.linspace(0,8,60)
y_axis=[]
for i in range(0,60):
	Y=A[i]*X+N
	p_y1=gauss(Y,A[i])
	p_y2=gauss(Y,-A[i])

plt.plot(A,p_y1,"g")
plt.plot(A,p_y2,"r")
plt.legend("p(y|x=1)","p(y|x=-1)")

plt.xlabel('$lambda$')
plt.ylabel('$P_A()$')
plt.show()