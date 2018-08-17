import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

def data_gen():

    t = 0
    x = []
    y = []
    with open("../data/heart-rate.csv" , "r") as file:
        reader = csv.reader(file , delimiter=",")
        reader.next()

        for row in reader:
            y.append(float(row[1]))
            x.append(t)
            t+=1
            yield x,y





def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()