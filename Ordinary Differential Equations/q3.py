import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

def plotPendulum():

    theta = [math.pi/4]
    omega = [0.0]
    h = 0.01 
    g = 9.81 # accerlation due to gravity
    L = 1.0 # length of pendulum

    tPoints = list(np.arange(0,10,h))

    for i in range(1,len(tPoints)):
        theta.append( theta[i-1] + omega[i-1] * h)
        omega.append( omega[i-1] - ( g / L )*math.sin( theta[i-1] ) * h )

    xPoints = list( L * np.sin(theta) )
    yPoints = list( -L * np.cos(theta) )

    fig, ax = plt.subplots()

    ax.set_xlim((-1.5, 1.5))

    ax.set_ylim((-1.5, 1.5))

    ax.set_aspect('equal')

    line, = ax.plot([], [], 'o-', lw=2)

    def animate(i):
        line.set_data([0, xPoints[i]], [0, yPoints[i]])
        return (line,)

    _ = FuncAnimation(fig, animate, frames= len(tPoints) , interval=h*1000, blit=True)
    plt.show()


if __name__=='__main__':

    plotPendulum()
