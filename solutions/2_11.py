import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

A=np.linspace(0,10,10)
Y=np.linspace(-10,10,400)

y_axis=[]
for i in range(0,10):
	p_y1=(1/np.sqrt(2*np.pi))*(np.exp(-np.square(Y-A[i])/2))

	p_y2=(1/np.sqrt(2*np.pi))*(np.exp(-np.square(Y+A[i])/2))
	plt.plot(Y,p_y1,"g")
	plt.plot(Y,p_y2,"r")
	
plt.xlabel('$lambda$')
plt.ylabel('$P_A()$')
plt.show()

# plt.legend("p(y|x=1)","p(y|x=-1)")

