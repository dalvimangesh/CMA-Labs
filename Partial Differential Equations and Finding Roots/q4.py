import math
import matplotlib.pyplot as plt

# define the function f(x) and its derivative f'(x)
def f(x):
    return x**3

def f_dash(x):
    return 3*(x**2)

# Secant Method to find the root of f(x)
def secantMethod(x0, x1, k):
    xValues = [x0, x1]

    for _ in range(k):
        xk = xValues[-1]
        xk_1 = xValues[-2]
        cur = xk - f(xk) * ((xk - xk_1) / (f(xk) - f(xk_1)))
        xValues.append(cur)

    return xValues

# Newton-Raphson Method to find the root of f(x)
def newtonRMethod(x0, k):
    xvals = [x0]

    for _ in range(k):
        xk = xvals[-1]
        cur = xk - (f(xk) / f_dash(xk))
        xvals.append(cur)

    return xvals

# calculate the rate of convergence for a sequence of approximations
def rateOfConvergence(xValues):
    values = []
    for i in range(2, len(xValues) - 1):
        Nr = math.log(
            abs((xValues[i + 1] - xValues[i]) / (xValues[i] - xValues[i - 1])))
        Dr = math.log(
            abs((xValues[i] - xValues[i - 1]) / (xValues[i - 1] - xValues[i - 2])))
        values.append(Nr / Dr)

    return values


if __name__ == '__main__':
    
    xSecant = secantMethod(100, 200, 50)
    xNewtonR = newtonRMethod(100, 50)

    # Calculate the rate of convergence for the two methods
    secandConv = rateOfConvergence(xSecant)
    newtonRConv = rateOfConvergence(xNewtonR)

    # Plot the rate of convergence for the two methods
    plt.title("Rate of Convergence")
    plt.ylabel('alpha')
    plt.xlabel("Iteration")
    plt.plot(list(range(2, len(secandConv) + 2)), secandConv, label="Secant Method")
    plt.plot(list(range(2, len(newtonRConv) + 2)), newtonRConv, label="Newton-Raphson Method")
    plt.legend()
    plt.grid()
    plt.show()