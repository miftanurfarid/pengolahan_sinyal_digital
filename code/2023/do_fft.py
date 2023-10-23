# -*- coding: utf-8 -*-

import numpy as np

xn = np.array([1,2,3,4,5,6,7,8])
print(xn)
Xk = np.fft.fft(xn)
print(Xk)
