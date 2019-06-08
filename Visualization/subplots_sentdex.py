import matplotlib.pyplot as plt
import random
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()


def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i;
        y = random.randrange(10)
        xs.append(x)
        ys.append(y)
    return xs, ys


"""Arguments passsed to add_subplot in order (left to right)_: length, width, plot_number
    Denotes the size of the mainplot"""
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

x, y = create_plots()
ax1.plot(x, y)

x, y = create_plots()
ax2.plot(x, y)

x, y = create_plots()
ax3.plot(x, y)

plt.show()
