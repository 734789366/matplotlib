import matplotlib.pyplot as plt
import numpy as np

n = 100
x, y = np.random.rand(2, n)
s = np.pi * (15 * np.random.rand(n)) ** 2
color = np.random.rand(n)

plt.scatter(x, y, s=s, c=color, alpha=0.6)
plt.show()