#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:12:39 2021

@author: fafa
"""

import numpy as np
import matplotlib.pyplot as plt

y = []

x = np.arange(-11,11,)

for i in range(len(x)+1):
    print('i=',i)
    print(f"x[{i}]={x}")

#y = np.asarray(y)

#plt.stem(x,y)

#plt.savefig('img001.svg', format='svg', dpi=1200)