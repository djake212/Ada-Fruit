#problem 2

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        self.t0 = time.perf_counter()
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.set_title("Sin(wt) over time")
        self.ax.set_xlabel("time(seconds)")
        self.ax.set_ylabel("sin(wt)")
        self.ax.add_line(self.line)
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        t,y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self):
        while True:
            t = time.perf_counter() - self.t0
            v = np.sin(np.pi*t)
            yield t,v

if __name__ == '__main__':
    dt = 0.01
    fig, ax = plt.subplots()
    scope = Scope(ax, maxt=10, dt=dt)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt*1000., blit=True)

    plt.show()