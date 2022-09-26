#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:23:50 2022

@author: fafa
"""
import matplotlib.pyplot as plt
import numpy as np

xn = [4,1,9,0,0,3,4,1,9,0,0,3,4,1,9,0,0,3]
n = np.arange(-5,len(xn)-5,1)
plt.stem(n,xn)
plt.xticks(n)
plt.xlabel('n')