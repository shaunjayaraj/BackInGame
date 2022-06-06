#! /Users/shaunjayaraj/.pyenv/shims/python

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
print(np.arange(50))
print(np.random.randint(10, 50,50))
print(np.random.randn(50))

plt.figure(1)
plt.plot([1,2,3,4],[1,7,3,5])
plt.show()

