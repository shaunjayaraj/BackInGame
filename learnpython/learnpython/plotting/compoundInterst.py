#! /Users/shaunjayaraj/.pyenv/shims/python

import matplotlib.pyplot as plt
import numpy as np


def plot(arr):
    plt.figure(1)
    plt.plot(arr, 'ko')
    plt.title("Compound interest growth")
    plt.xlabel("years")
    plt.ylabel("Principal")
    plt.show()


principal = 100000
interestRate = 0.02
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += (principal * interestRate)

print(values)
plot(values)



