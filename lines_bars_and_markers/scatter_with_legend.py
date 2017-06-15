import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
for color in ['red', 'green', 'blue']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0*np.random.rand(n)
    ax.scatter(x, y, c=color, label=color, s=scale, alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)
plt.show()