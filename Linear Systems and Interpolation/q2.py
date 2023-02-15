from q1 import RowVectorFloat
from random import uniform
import numpy as np
import sys

# Function to check for any exception in inputFunction
def Check(inputFunction):

    # Function to handle the exception
    def newFunction(ref, *arg, **kwargs):
        try:
            return inputFunction(ref, *arg, **kwargs)
        except Exception as e:
            print(type(e))
            print(e)
            sys.exit(-1)

    return newFunction

class SquareMatrixFloat:

    @Check
    def __init__(self, n) -> None:

        if type(n) is not int:
            raise Exception('Diamension should be non negative integer')

        self.n = n # storing the dimension of the square matrix
        self.squareMatrix = list() # initializing an empty list

        # creating emppty square matrix
        for _ in range(n):
            self.squareMatrix.append(RowVectorFloat([0]*n))

    # Function to return string form of class
    def __str__(self) -> str:
        res = "The matrix is:\n"
        for row in self.squareMatrix:
            res += str(row) + '\n'
        return res

    # Function to fill the square matrix with random values and make it symmetric
    def sampleSymmetric(self) -> None:

        '''
        samples a random symmetric matrix
        of size n * n such that 
        >>> aij = aji = Uniform(0, 1) for i != j, and 
        >>> aii = Uniform(0, n).
        '''

        for i in range(0, self.n):
            for j in range(i, self.n):
                self.squareMatrix[i][j] = self.squareMatrix[j][i] = uniform(0, self.n) if i == j else uniform(0, 1)

    # Convert the matrix to row echelon form
    def toRowEchelonForm(self) -> None:

        x, y = 0, 0

        while x < self.n and y < self.n:

            tempX = x

            # Find the first row with a non-zero element in the column y
            while tempX < self.n and self.squareMatrix[tempX][y] == 0:
                tempX += 1

            # If no such row exists then move to the next column
            if tempX == self.n:
                y += 1
                continue
            else: # swapping the rows to make the current pivot element non-zero
                self.squareMatrix[x][y], self.squareMatrix[tempX][y] = self.squareMatrix[tempX][x], self.squareMatrix[x][y]

            # Making current pivot equals to 1
            self.squareMatrix[x] = self.squareMatrix[x] * (1/self.squareMatrix[x][y])

            for row in range(x+1,self.n): # Subtract the current row from all rows below it to eliminate the element in column y
                self.squareMatrix[row] = self.squareMatrix[row] + ( -1 * self.squareMatrix[row][y] ) * self.squareMatrix[x]

            # going for next pivot
            x+=1
            y+=1
    
    # checks if the matrix is diagonally row dominant
    def isDRDominant(self) -> bool:

        for i in range(self.n):
            dig = self.squareMatrix[i][i]
            rowSum = self.squareMatrix[i].sum() - dig
            if dig <= rowSum:
                return False
        return True

    # Function return the list of error values and the final solution array
    @Check
    def performIterations(self, b, iterations,isJacobi=True):

        # if the matrix is not diagonally dominant and the method is Jacobi, then we cannot use this method.
        if isJacobi and not self.isDRDominant():
            raise Exception('Not solving because convergence is not guranteed')

        prevX = [0] * self.n # to store previous solution, at start it's zero
        error = [] # to store error values for each iteration

        for _ in range(iterations):

            curX = [0] * self.n # # current solution array, initialized with zeros

            for i in range(self.n):

                numerator = b[i]

                for j in range(self.n):

                    if i == j:
                        continue
                    else:
                        if isJacobi: # Jacobi method: use the previous solution array
                            numerator -= ( self.squareMatrix[i][j] * prevX[j] )

                        else:  # Gauss-Seidel method: use the current solution array for elements that have already been computed
                            if i < j:
                                numerator -= ( self.squareMatrix[i][j] * prevX[j] )
                            else:
                                numerator -= ( self.squareMatrix[i][j] * curX[j] )
            
                # update the current solution array for the current row
                curX[i] = numerator / self.squareMatrix[i][i]
            
            # compute the error for the current iteration
            AX_B = []
            for i in range(self.n):
                val = 0
                for j in range(self.n):
                    val += self.squareMatrix[i][j] * curX[j]
                AX_B.append(val-b[i])

            # append the error value to the list of error values
            error.append ( np.linalg.norm( np.array(AX_B), ord=2 ))

            # updating for next interation
            prevX = curX

        return error,prevX
    
    # Jacobi method
    @Check
    def jSolve(self,b,iterations):

        if type(b) is not list or not all((type(i) is float or type(i) is int) for i in b) or (len(b) != self.n):
            raise Exception('Input must be list of length '+ str(self.n) + ' and all elements must be either float or int')

        if type(iterations) is not int or iterations < 0:
            raise Exception('Iterations should be non negative integer')
        
        return self.performIterations(b,iterations=iterations)

    # Gauss-Seidel method
    def gsSolve(self,b,iterations):

        if type(b) is not list or not all((type(i) is float or type(i) is int) for i in b) or (len(b) != self.n):
            raise Exception('Input must be list of length '+ str(self.n) + ' and all elements must be either float or int')

        if type(iterations) is not int or iterations < 0:
            raise Exception('Iterations should be non negative integer')
                
        return self.performIterations(b,iterations=iterations,isJacobi=False)

if __name__ == '__main__':

    # s = SquareMatrixFloat(4)
    # s.sampleSymmetric()
    # print(s.isDRDominant())
    # print(s)

    # s = SquareMatrixFloat(4)
    # s.sampleSymmetric()
    # (e, x) = s.jSolve([1, 2, 3, 4], 10)
    # print(x)
    # print(e)

    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    (err, x) = s.gsSolve([1, 2, 3, 4], 10)
    print(x)
    print(err)