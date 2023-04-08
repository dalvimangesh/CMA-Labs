import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp


def solveThreeBody(t0, y0):

    '''
    Function that takes the initial position of the 3 bodies as its argument, and visualizes
    their trajectories
    '''

    # Function to calculate double derivatives with help of given equations
    def doubledd(r1, r2, r3): return list((r2 - r1)/( max(np.linalg.norm(r2-r1),2)** 3) + (r3 - r1)/( max(np.linalg.norm(r3-r1),2)**3))

    # Define the differential equation system
    def f(t, y):

        r1x, r1y, r2x, r2y, r3x, r3y, v1x, v1y, v2x, v2y, v3x, v3y = y
        r1 = np.array([r1x, r1y])
        r2 = np.array([r2x, r2y])
        r3 = np.array([r3x, r3y])
        v1 = [v1x, v1y]
        v2 = [v2x, v2y]
        v3 = [v3x, v3y]
        v1d = doubledd(r1, r2, r3)
        v2d = doubledd(r2, r3, r1)
        v3d = doubledd(r3, r1, r2)
        l = v1 + v2 + v3 + v1d + v2d + v3d
        return l

    tPoints = np.linspace(t0, 100, 1000)

    # Solve the Van der Pol equation using initial conditions y0, time span [t0, 100], and time points t_eval
    sol = solve_ivp(fun=f, t_span=[t0, 100], y0=y0, t_eval=tPoints)

    r1x, r1y, r2x, r2y, r3x, r3y = sol.y[0],sol.y[1],sol.y[2],sol.y[3],sol.y[4],sol.y[5]
    

    # Results
    fig, ax = plt.subplots()
    ax.set_xlim((-1, 5))
    ax.set_ylim((-3.5, 3.5))
    ax.set_aspect('equal')

    body1 = ax.add_patch(plt.Circle((r1x[0], r1y[0]), 0.05, fc="r", label="Point1"))
    body2 = ax.add_patch(plt.Circle((r2x[0], r2y[0]), 0.05, fc="b", label="Point2"))
    body3 = ax.add_patch(plt.Circle((r3x[0], r3y[0]), 0.05, fc="g", label="Point3"))

    patches = [body1,body2,body3]

    def animate(i):
        
        body1.set_center((r1x[i], r1y[i]))
        body2.set_center((r2x[i], r2y[i]))
        body3.set_center((r3x[i], r3y[i]))

        return patches

    _ = FuncAnimation(fig, animate, frames= len(r1x) , interval=1, blit=True)
    # _.save('q5.gif')
    plt.show()


if __name__ == '__main__':

    t0 = 5
    y0 = [ 0 , 0, 1.3, 2.73 , 2.3, -1.73 , 0 , 0 , 0 ,0 , 0 , 0  ]

    solveThreeBody(t0=0, y0=y0)
