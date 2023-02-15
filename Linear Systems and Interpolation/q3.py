from q2 import SquareMatrixFloat
from random import randint
import matplotlib.pyplot as plt

def visualizeConvergence(dia=10, iterations = 50):

    '''
    function to visualize rate of convergence of Jacobi and Gauss-Siedel methods 
    of a linear system with a diagonally dominant square symmetric matrix
    '''

    matrix = SquareMatrixFloat(dia)
    matrix.sampleSymmetric()

    # while we are not getting diagonally row dominant to make sure jacobi method convergence
    while not matrix.isDRDominant():
        matrix.sampleSymmetric()

    # generating random integers
    b = [ randint(1,dia) for _ in range(dia) ]

    xPoints = list(range(1,iterations+1))

    # to plot the error return for each iterations by each method
    y1Points,_ = matrix.jSolve(b=b,iterations=iterations)
    y2Points,_ = matrix.gsSolve(b=b,iterations=iterations)

    # Ploting the graph
    plt.plot(xPoints, y1Points,label='Jacobi method')
    plt.plot(xPoints, y2Points,label='Gauss-Siedel method')
    plt.xlabel('No of iterations')
    plt.ylabel('||Ax⁽ᵏ⁾ - b||₂')
    plt.title('rate of convergence of Jacobi and Gauss-Siedel')
    plt.legend(frameon=True, fontsize=11)
    plt.grid()
    plt.show()

if __name__=='__main__':

    visualizeConvergence()