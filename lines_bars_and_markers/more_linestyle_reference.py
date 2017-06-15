import matplotlib.pyplot as plt
import numpy as np

color = 'blue'
points = np.ones(5) # Draw 5 points for each line
text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'monospace'})

def format_axes(ax):
    ax.margins(0.99)
    # ax.set_axis_off()

def nice_repr(text):
    return repr(text).lstrip('u')

fig, ax = plt.subplots()

linestyles = ['-', '--', '-.', ':']
for y, linestyle in enumerate(linestyles):
    ax.text(-0.1, y, nice_repr(linestyle), **text_style)
    print (y * points)
    ax.plot(y * points, linestyle=linestyle, color=color, linewidth=3)
    format_axes(ax)
    ax.set_title('line style')

plt.show()