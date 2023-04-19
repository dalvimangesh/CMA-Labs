import math
import matplotlib.pyplot as plt


# TODO Change function
def f(x):
    return x * math.exp(-x)


def f_dash(x):
    return -x * math.exp(-x) + math.exp(-x)


def secantMethod(x0, x1, k):

    xValues = [x0, x1]

    for _ in range(k):
        xk = xValues[-1]
        xk_1 = xValues[-2]
        cur = xk - f(xk) * ((xk - xk_1) / (f(xk) - f(xk_1)))
        xValues.append(cur)

    return xValues


def newtonRMethod(x0, k):

    xvals = [x0]

    for _ in range(k):
        xk = xvals[-1]
        cur = xk - (f(xk) / f_dash(xk))
        xvals.append(cur)

    return xvals


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

    xSecant = secantMethod(2, 3, 100)
    xNewtonR = newtonRMethod( 2, 100 )

    secandConv = rateOfConvergence( xSecant )
    newtonRConv = rateOfConvergence ( xNewtonR )

    plt.title("Rate of Convergence")
    # plt.ylabel(`α')
    plt.xlabel("Iteration")
    plt.plot(list(range(2, len(secandConv) + 2)), secandConv, label="Secant Method")
    plt.plot(list(range(2, len(newtonRConv) + 2)), newtonRConv, label="Newton-Raphson Method")
    plt.legend()
    plt.grid()
    plt.show()

