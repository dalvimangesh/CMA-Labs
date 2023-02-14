from q2 import SquareMatrixFloat
from random import randint
import matplotlib.pyplot as plt

def visualizeConvergence(dia=10, iterations = 30):

    matrix = SquareMatrixFloat(dia)
    matrix.sampleSymmetric()
    while not matrix.isDRDominant():
        matrix.sampleSymmetric()

    b = [ randint(1,dia) for _ in range(dia) ]

    xPoints = list(range(1,iterations+1))

    y1Points,_ = matrix.jSolve(b=b,iterations=iterations)
    y2Points,_ = matrix.gsSolve(b=b,iterations=iterations)

    plt.plot(xPoints, y1Points,label='Jacobi method')
    plt.plot(xPoints, y2Points,label='Gauss-Siedel method')
    plt.xlabel('No of iterations')
    plt.ylabel('||Ax⁽ᵏ⁾ - b||₂')
    plt.legend(frameon=True, fontsize=11)
    plt.grid()
    plt.show()

if __name__=='__main__':

    visualizeConvergence()