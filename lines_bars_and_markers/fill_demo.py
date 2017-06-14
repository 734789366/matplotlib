import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.sin(4*x)

plt.fill(x, y1, 'r', x, y2, 'g')
plt.show()