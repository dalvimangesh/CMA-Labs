from q1 import RowVectorFloat
from random import uniform
import numpy as np


class SquareMatrixFloat:

    def __init__(self, n) -> None:

        self.n = n
        self.squareMatrix = list()
        for _ in range(n):
            self.squareMatrix.append(RowVectorFloat([0]*n))

    def __str__(self) -> str:
        res = "The matrix is:\n"
        for row in self.squareMatrix:
            res += str(row) + '\n'
        return res

    def sampleSymmetric(self):

        for i in range(0, self.n):
            for j in range(i, self.n):
                self.squareMatrix[i][j] = self.squareMatrix[j][i] = uniform(0, self.n) if i == j else uniform(0, 1)

    def toRowEchelonForm(self):

        x, y = 0, 0

        while x < self.n and y < self.n:

            tempX = x
            while tempX < self.n and self.squareMatrix[tempX][y] == 0:
                tempX += 1

            if tempX == self.n:
                y += 1
                continue
            else:
                self.squareMatrix[x][y], self.squareMatrix[tempX][y] = self.squareMatrix[tempX][x], self.squareMatrix[x][y]

            # Making current pivot equals to 1
            self.squareMatrix[x] = self.squareMatrix[x] * (1/self.squareMatrix[x][y])

            for row in range(x+1,self.n):
                self.squareMatrix[row] = self.squareMatrix[row] + ( -1 * self.squareMatrix[row][y] ) * self.squareMatrix[x]

            # going for next pivot
            x+=1
            y+=1
    
    def isDRDominant(self) -> bool:

        for i in range(self.n):
            dig = self.squareMatrix[i][i]
            rowSum = sum(self.squareMatrix[i]) - dig
            if dig <= rowSum:
                return False

        return True

    def performIterations(self, b, iterations,isJacobi=True):

        if isJacobi and not self.isDRDominant():
            return [],[]

        prevX = [0] * self.n
        error = []

        for _ in range(iterations):

            curX = [0] * self.n

            for i in range(self.n):

                numerator = b[i]

                for j in range(self.n):

                    if i == j:
                        continue
                    else:
                        if isJacobi:
                            numerator -= ( self.squareMatrix[i][j] * prevX[j] )
                        else:
                            if i < j:
                                numerator -= ( self.squareMatrix[i][j] * prevX[j] )
                            else:
                                numerator -= ( self.squareMatrix[i][j] * curX[j] )
            
                curX[i] = numerator / self.squareMatrix[i][i]
            
            AX_B = []
            for i in range(self.n):
                val = 0
                for j in range(self.n):
                    val += self.squareMatrix[i][j] * curX[j]
                AX_B.append(val-b[i])

            error.append ( np.linalg.norm( np.array(AX_B), ord=2 ))

            prevX = curX

        return error,prevX
    
    def jSolve(self,b,iterations):
        return self.performIterations(b,iterations=iterations)

    def gsSolve(self,b,iterations):
        return self.performIterations(b,iterations=iterations,isJacobi=False)

if __name__ == '__main__':
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    (err, x) = s.gsSolve([1, 2, 3, 4], 10)
    print(x)
    print(err)
