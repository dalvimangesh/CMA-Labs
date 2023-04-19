import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the constants
L = 1.0  # Length of the rod
alpha = 0.01  # Thermal diffusivity

# Define the initial condition
def initial_condition(x):
    return np.exp(-x) * (1 - np.logical_or(x==0, x==L))

# Define the PDE
def heat_conduction_pde(t, u):
    dudt = np.zeros_like(u)
    dudt[1:-1] = alpha * (u[2:] - 2 * u[1:-1] + u[:-2]) / ((L / (len(u) - 1)) ** 2)
    dudt[0] = 0
    dudt[-1] = 0
    return dudt

# Define the time range and the number of spatial points
t_span = (0, 5)
N = 100

# Create the spatial grid
x = np.linspace(0, L, N)

# Solve the PDE using the initial condition
sol = solve_ivp(heat_conduction_pde, t_span, initial_condition(x), t_eval=np.linspace(t_span[0], t_span[1], 200))

# Define the animation function
def animate(i):
    plt.clf()
    plt.imshow(sol.y[:, [i]].T, cmap='Reds', extent=[0, L, 0, 1], aspect=L)
    plt.title(f"Time: {sol.t[i]:.2f}")
    plt.xlabel("Position")
    plt.ylabel("Temperature")

# Create the animation
fig = plt.figure(figsize=(6, 4))
ani = FuncAnimation(fig, animate, frames=len(sol.t), interval=50)

# Show the animation
plt.show()
