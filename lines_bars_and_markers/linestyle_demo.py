import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]

line1, = plt.plot(x, np.sin(x), '--', label='Dashes set retroactively')
line1.set_dashes(dashes)
line12 = plt.plot(x, np.cos(x), dashes=[30, 5, 10, 5])
plt.legend('upper right')

plt.show()