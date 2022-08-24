#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:33:29 2021

@author: fafa
"""

import matplotlib.pyplot as plt
import numpy as np

# Plot a sine and cosine curve
fig, ax = plt.subplots()
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
ax.plot(x, np.cos(x) + 1, lw=3)

# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)

def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == -1:
        return r"$-\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
fig

plt.savefig('plot_cosine.svg', format='svg', dpi=1200)