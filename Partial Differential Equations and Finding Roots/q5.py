import math
import matplotlib.pyplot as plt
import scipy.linalg as linalg


def f(x):
    x1, x2, x3 = x
    fx1 = 3 * x1 - math.cos(x2 * x3) - (3 / 2)
    fx2 = 4 * (x1**2) - 625 * (x2**2) + 2 * x3 - 1
    fx3 = 20 * x3 + math.exp(-1 * x1 * x2) + 9
    return [fx1, fx2, fx3]


def fJocobi(x):
    x1, x2, x3 = x
    j1 = [3, x3 * math.sin(x2 * x3), x2 * math.sin(x2 * x3)]
    j2 = [8 * x1, -1250 * x2, 2]
    j3 = [-x2 * math.exp(-1 * x1 * x2), -x1 * math.exp(-1 * x1 * x2), 20]
    return [j1, j2, j3]


def newtonRMethod(x0, k):

    xvals = [x0]

    for _ in range(k):
        xk = xvals[-1]
        cur = xk - (linalg.inv(fJocobi(xk)) @ f(xk))
        xvals.append(cur)
    return xvals


if __name__ == "__main__":

    xNR = newtonRMethod([1, 2, 3], 20)

    print(f"The root of the function is {xNR[-1]}")

    # Evaluating the norm of the function at the obtained points
    fNR = [linalg.norm(f(x)) for x in xNR]

    # Plotting the rate of convergence
    plt.title("||f(xₖ)|| vs Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("||f(xₖ)||")
    plt.plot(list(range(0, len(xNR))), fNR, label="Newton-Raphson Method")
    plt.legend()
    plt.grid()
    plt.show()
