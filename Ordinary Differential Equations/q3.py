import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math


def plotPendulum():

    # Initial conditions
    theta = [math.pi/4]  # initial angle of the pendulum
    omega = [0.0]  # initial angular velocity of the pendulum
    h = 0.01  # time step
    g = 9.81  # accerlation due to gravity
    L = 1.0  # length of pendulum

    tPoints = list(np.arange(0, 10, h))

    # using Forward Euler method
    for i in range(1, len(tPoints)):
        theta.append(theta[i-1] + omega[i-1] * h)
        omega.append(omega[i-1] - (g / L)*math.sin(theta[i-1]) * h)

    # x-coordinates of the pendulum bob
    xPoints = list(L * np.sin(theta))
    # y-coordinates of the pendulum bob
    yPoints = list(-L * np.cos(theta))

    fig, ax = plt.subplots()
    ax.set_xlim((-1.5, 1.5))
    ax.set_ylim((-1.5, 1.5))
    ax.set_aspect('equal')
    line, = ax.plot([], [], 'o-', lw=2)

    def animate(i):
        line.set_data([0, xPoints[i]], [0, yPoints[i]])
        return (line,)

    # create an animation using the line object and update function
    _ = FuncAnimation(fig, animate, frames=len(tPoints), interval=h*1000, blit=True)
    # _.save('q3.gif')
    plt.show()


if __name__ == '__main__':

    plotPendulum()
