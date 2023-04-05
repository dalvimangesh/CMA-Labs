import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks


def solveVanDarPolEquation(mu, t0, y0):

    def f(t, y):
        x, v = y
        return [v, mu * (1 - x * x) * v - x]

    tPoints = np.linspace(t0, 100, 1000)

    sol = solve_ivp(fun=f, t_span=[t0, 100], y0=y0, t_eval=tPoints)

    xPoints = sol.y[0]

    plt.title(f"Van Der Pol Equation for μ = {mu}")
    plt.ylabel("x(t)")
    plt.xlabel("t")
    plt.plot(tPoints, xPoints)
    plt.grid()
    plt.show()

    peaks, _ = find_peaks(xPoints)
    period = np.mean(np.diff(tPoints[peaks]))
    print(f"The time period of the curve for μ = {mu} is {period}")


if __name__ == '__main__':

    mu = 0.1
    t0 = 1.0
    y0 = [0, 5]

    solveVanDarPolEquation(mu=0, t0=0, y0=y0)
