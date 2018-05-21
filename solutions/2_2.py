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
A=4
Y=A*X+N

plt.plot(Y,'o')
plt.xlabel('$Sample}$')
plt.ylabel('$Y$')
plt.show()