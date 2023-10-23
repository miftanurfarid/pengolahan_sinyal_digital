import numpy as np
from matplotlib import pylab


xn = np.array([3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2])
start = -3
n = np.arange(start, len(xn)+start)
print(len(n))
print(len(xn))

pylab.stem(n, xn, )
pylab.grid()
pylab.xlabel('n', size=14)
pylab.ylabel('x(n)', size=14)
pylab.show()
