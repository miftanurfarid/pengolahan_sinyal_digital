import numpy as np
import matplotlib.pyplot as plt

xn = np.zeros(20)
xn[7:12] = np.arange(0.2,1.2,0.2)
xn[11:16] = np.arange(1,0,-0.2)
filename = '../../../img/2022/02.dft/01.finite_length_sequence.svg'

plt.stem(xn)
plt.ylabel(r'x(n)')
plt.xlabel(r'n')
plt.savefig(filename, format='svg', dpi=1200)