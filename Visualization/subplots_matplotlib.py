import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
"""Arguments of subplots in order: rowspan =2, colspan=1"""
fig, ax = plt.subplots(2, 1, figsize=(5, 10))
ax[0].plot(x, y)
ax[0].set_title('A single plot')
ax[1].plot(x, y)
ax[1].set_title('Another plot')
plt.show()
