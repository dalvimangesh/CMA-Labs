import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Akima1DInterpolator, BarycentricInterpolator, CubicSpline
from matplotlib.animation import FuncAnimation

# sample function
def true(x):
    return (np.tan(x) * np.sin(30 * x)) * np.exp(x)

# Define the function that will update the plot for each frame of the animation
def update(frameNum):
    
    xPoints = np.linspace(-4, 4, frameNum)
    yPoints = true(xPoints)

    # Calculating the true function values for the x-axis
    yOfTrue = true(x)

    # Update the lines with the interpolated values for this frame

    cubicLine.set_data(x, CubicSpline(xPoints, yPoints)(x) )
    akimaLine.set_data(x, Akima1DInterpolator(xPoints, yPoints)(x) )
    baryLine.set_data(x, BarycentricInterpolator(xPoints, yPoints)(x))

    trueLine.set_data(x, yOfTrue)
    ax.set_title(f'Interpolations of tan(x)*sin(30*x)*exp(x), Frame : {frameNum/5}')


if __name__ == '__main__':

    x = np.linspace(0, 1, 10000) # Generate 10000 points between (0,1)

    points = np.arange(5, 300, 5) # Generate a list of the number of points to sample for the animation

    fig, ax = plt.subplots() # figure and axes for the animation

    # Define the empty line objects for the interpolations
    cubicLine, = ax.plot([], [], label="Cubic spline",color='red')
    akimaLine, = ax.plot([], [], label="Akima",color='green')
    baryLine, = ax.plot([], [], label="Barycentric",color='purple')
    trueLine, = ax.plot([], [], label="True",color='blue')

    #Plot details
    ax.set_title("Interpolations of Sample Function")
    ax.grid()
    ax.legend()
    ax.set_xlim(0, 1)
    ax.set_ylim(-4, 4)
    animation = FuncAnimation(fig, update, frames=points)
    #animation.save('q5.gif')
    plt.show() # result
