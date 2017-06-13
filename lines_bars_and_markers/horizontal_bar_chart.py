"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""

import matplotlib.pyplot as plt
import numpy as np

# reset plt的参数
plt.rcdefaults()

# 创建一个figure和若干subplot
fig, ax = plt.subplots()
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
print(performance)
print(error)
# 创建一个horizontal bar图，参数为y位置，y值，xerr，对齐方式，颜色
ax.barh(y_pos, performance, xerr=error, align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('performance')
ax.set_title('How fast do you want to go today?')
plt.show()