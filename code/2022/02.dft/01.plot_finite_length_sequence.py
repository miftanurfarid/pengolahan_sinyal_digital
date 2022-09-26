import numpy as np
import matplotlib.pyplot as plt

# Plot Finite Lenght Sequence
xn = np.zeros(20)
n  = np.arange(-6,14,1)
xn[7:12] = np.arange(0.2,1.2,0.2)
xn[11:16] = np.arange(1,0,-0.2)
filename = '../../../img/2022/02.dft/01.finite_length_sequence.svg'

plt.stem(n,xn)
plt.grid()
plt.ylabel(r'x(n)')
plt.xlabel(r'N-1 n')
plt.xticks(n)
figure1 = plt.gcf()  # get current figure
figure1.set_size_inches(10, 4) 
#plt.savefig(filename, format='svg', dpi=1200)

# Plot Periodic Sequence
filename2 = '../../../img/2022/02.dft/02.periodic_sequence.svg'
xn1 = np.arange(0,1.2,0.2)
xn1 = np.append(xn1, np.arange(0.8,0,-0.2))
xn2 = np.append(xn1,xn1)
xn2 = np.append(xn2,xn1)
n2 = np.arange(-10,len(xn2)-10,1)
plt.stem(n2,xn2)
plt.ylabel(r'x(n)')
plt.xlabel(r'N-1 n')
plt.xticks(n2)
figure2 = plt.gcf()  # get current figure
figure2.set_size_inches(10, 4) 
plt.grid()
#plt.savefig(filename2, format='svg', dpi=1200, bbox_inches='tight')