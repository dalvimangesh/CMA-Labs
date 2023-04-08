import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks


def solveVanDarPolEquation(mu, t0, y0):
    '''
    function that takes the parameter μ (a positive real number) and initial condition as arguments,
    and computes period of the limit cycle.
    '''

    # Define the differential equation system
    def f(t, y):
        x, v = y
        return [v, mu * (1 - x * x) * v - x]

    tPoints = np.linspace(t0, 100, 1000)

    # Solve the Van der Pol equation using initial conditions y0, time span [t0, 100], and time points t_eval
    sol = solve_ivp(fun=f, t_span=[t0, 100], y0=y0, t_eval=tPoints)

    # Extract the x values from the solution
    xPoints = sol.y[0]

    # Find the peaks in xPoints
    peaks, _ = find_peaks(xPoints)
    # Calculate the average period between the peaks
    period = np.mean(np.diff(tPoints[peaks]))

    # Results
    plt.title(f"Van Der Pol Equation for μ = {mu}")
    plt.ylabel("p(x)")
    plt.xlabel("x")
    plt.plot(tPoints, xPoints)
    plt.grid()
    plt.show()
    print(f"The time period for μ = {mu} is {period}")


if __name__ == '__main__':

    mu = 0.1
    t0 = 1.0
    y0 = [0, 5]

    solveVanDarPolEquation(mu=0, t0=0, y0=y0)
