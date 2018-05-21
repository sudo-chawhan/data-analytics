import numpy as np
from scipy import special
import matplotlib.pyplot as plt
A = np.linspace(1, np.sqrt(10),20)
sample = int(1e5)
err = []
n = np.random.normal(0,1,sample)
for i in range(0,20):
    err_ind = np.nonzero(-n > A[i])
    err_n = np.size(err_ind)
    err.append(err_n/sample)

plt.semilogy(A, special.erfc(A/np.sqrt(2))/2,'o')
plt.semilogy(A, err)

plt.xlabel('$x$')
plt.ylabel('$erfc(x)$')
plt.show()