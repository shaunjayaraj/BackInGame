#! /Users/shaunjayaraj/.pyenv/shims/python

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)  # seed the random number generator.
data1 = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data1['b'] = data1['a'] + 10 * np.random.randn(50)
data1['d'] = np.abs(data1['d']) * 100

fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data1)
ax.set_xlabel('Some parameter')
ax.set_ylabel('Other parameter')
ax.legend()
plt.show()