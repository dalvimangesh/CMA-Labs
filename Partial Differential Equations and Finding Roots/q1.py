import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import numpy as np

# define the initial temperature distribution
def initialCondition(x, L):
    u = []
    for i in range(len(x)):
        if x[i] == 0 or x[i] == L:
            u.append(0)
        else:
            u.append(np.exp(-x[i]))
    return u


# Define the PDE for heat conduction
def heatConductionPDE(t, u, mu, L):
    du_dt = []
    dx = L / (len(u) - 1)
    du_dt.append(0)
    for i in range(1, len(u) - 1):
        du_dt_i = mu * (u[i+1] - 2 * u[i] + u[i-1]) / dx**2
        du_dt.append(du_dt_i)
    du_dt.append(0)
    return du_dt


if __name__ == '__main__':

    L = 1.0  # length of the rod
    mu = 0.01  # thermal diffusivity
    t_span = (0, 5)  # time interval for simulation
    N = 100  # number of spatial grid points
    x = np.linspace(0, L, N)  # spatial grid

    # solve the PDE using the initial condition and time span
    u0 = initialCondition(x, L)
    sol = solve_ivp(lambda t, u: heatConductionPDE(t, u, mu, L), t_span, u0, t_eval=np.linspace(t_span[0], t_span[1], 200))

    # Result
    fig = plt.figure(figsize=(6, 4))

    def animate(i):
        plt.clf()
        u = sol.y[:, i]
        plt.plot(x, u, color='red')
        plt.xlim([0, L])
        plt.ylim([0, 1])
        plt.xlabel("Position")
        plt.ylabel("Temperature")
        plt.title(f"Time: {sol.t[i]:.2f}")

    _ = FuncAnimation(fig, animate, frames=len(sol.t), interval=50)
    # _.save('q1.gif')
    plt.show()
