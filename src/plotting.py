import csv
import matplotlib.pyplot as plt
import datetime

t=0
x = []
y = []
with open("../data/heart-rate.csv" , "r") as file:
    plots = csv.reader(file ,delimiter=",")

    plots.next()
    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()

    for row in plots:

        y.append(float(row[1]))
        x.append(row[0])
        
        plt.pause(0.001)
        plt.plot(x,y, label='Data!')
        fig.canvas.draw()

        # draw the figure so the animations will work




plt.xlabel('x')
plt.ylabel('y')
plt.title('ECG')
plt.legend()
plt.show()

    