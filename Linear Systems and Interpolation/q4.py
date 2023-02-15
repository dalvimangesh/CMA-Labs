import numpy as np
import matplotlib.pyplot as plt
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

class Polynomial:

    @Check
    def __init__(self, coefficients) -> None:

        if type(coefficients) is not list or not all((type(i) is float or type(i) is int or type(i) is np.float64) for i in coefficients):
            raise Exception('Input must be list and all elements must be either float or int')

        self.coefficients = coefficients
        self.degree = max(0,len(coefficients)-1)

    # Returns string form the Polynomial class
    def __str__(self) -> str:
        res = 'Coefficients of the polynomial are:\n' + \
            " ".join(str(i) for i in self.coefficients)
        return res

    # Polynomial addition
    def __add__(self, p):

        # creating empty list with all zero and adding corresponding degree terms to it
        tempCoeff = [0] * max(self.degree + 1, p.degree + 1)

        for index, val in enumerate(self.coefficients):
            tempCoeff[index] += val

        for index, val in enumerate(p.coefficients):
            tempCoeff[index] += val

        return Polynomial(tempCoeff)

    # Polynomial subtraction
    def __sub__(self, p):

        # creating empty list with all zero and adding corresponding degree terms of self and substracting from p
        tempCoeff = [0] * max(self.degree+1, p.degree+1)

        for index, val in enumerate(self.coefficients):
            tempCoeff[index] += val

        for index, val in enumerate(p.coefficients):
            tempCoeff[index] -= val

        return Polynomial(tempCoeff)

    # Polynomial multiplication
    def __mul__(self, operand):
        tempCoeff = []
        if type(operand) is Polynomial:
            tempCoeff = self.__polyMul(operand)
        else:
            tempCoeff = self.__scalarMul(operand)
        return Polynomial(tempCoeff)

    # Polynomial multiplication
    def __rmul__(self, operand):
        return self.__mul__(operand)

    # evaluate the polynomial at any real number and returns result
    def __getitem__(self, x) -> float:
        res = 0
        for i, c in enumerate(self.coefficients):
            res += c * (x**i)
        return res

# Private

    # Multiply each coefficient by scalar and returns list
    def __scalarMul(self, scalar) -> list:
        tempCoeff = []
        for i in self.coefficients:
            tempCoeff.append(i*scalar)
        return tempCoeff

    # Multiply two polynomial
    def __polyMul(self, p) -> list:

        tempCoeff = dict() # sotring coefficient of ith degree at key = i

        # performing multiplication
        for coef1 in range(self.degree+1):
            for coef2 in range(p.degree+1):
                if coef1+coef2 not in tempCoeff:
                    tempCoeff[coef1+coef2] = 0
                tempCoeff[coef1+coef2] += self.coefficients[coef1] * \
                    p.coefficients[coef2]

        return [val for _, val in tempCoeff.items()]

    def __getTitle(self) -> str:

        # Returns the superscript representation of a positive integer
        def getSuperscript( n: int ) -> str:
            superscript_digits = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
            # use str.translate to replace each digit with its corresponding superscript
            return str(n).translate(superscript_digits)

        res = "" # Result
        isFirst = True # flag to store wheather we have added at least one term in res or not



        '''
        checks for special cases such as negative coefficients and coefficient equal to 1.
        Finally, the function returns the result string. 
        If no terms were added to the result, the function returns a string representation of 0
        '''

        for power, value in enumerate(self.coefficients):

            if value == 0: # not adding terms having zero coefficient
                continue

            curCoeff = round(value, 2)

            if power == 0:
                res += str(curCoeff)
            elif power == 1: # for power 1, not writing 1 at power place
                if isFirst: 
                    if curCoeff == -1:
                        res += '-' + 'x'
                    elif curCoeff == 1:
                        res += 'x'
                    else:
                        res += str(curCoeff) + 'x'
                else:
                    if curCoeff == -1:
                        res += ('-' + 'x')
                    elif curCoeff == 1:
                        res += ('+' + 'x')
                    else:
                        res += ('+' + str(curCoeff) +'x') if curCoeff >= 0 else (str(curCoeff) + 'x')
            else:
                if isFirst:
                    if curCoeff == -1:
                        res += ( '-' + 'x' + getSuperscript(power) )
                    elif curCoeff == 1:
                        res += ( 'x' + getSuperscript(power) )
                    else:
                        res += (str(curCoeff) + 'x' + getSuperscript(power))
                else:
                    if curCoeff == -1:
                        res += ('-' + 'x' + getSuperscript(power))
                    elif curCoeff == 1:
                        res += ('+' + 'x' + getSuperscript(power))
                    else:
                        res += ('+' + str(curCoeff) + 'x' + getSuperscript(power)) if curCoeff >= 0 else (str(curCoeff) + 'x' + getSuperscript(power))

            isFirst = False

        if isFirst: res = str(0)
        return res # result

# Public

    # function to visualize the polynomial in any interval of the type [a, b]
    def show(self, low, high, toShow=True):

        xPoints = list(np.linspace(low, high, 100)) # creating 100 uniform points in range [low,high]
        yPoints = list(map(self.__getitem__, xPoints)) # list of polynomail value at each xPoints

        # Ploting
        plt.plot(xPoints, yPoints, color='blue')
        plt.xlabel('x')
        plt.ylabel('p(x)')
        plt.title("Plot of the polynomial " + self.__getTitle())
        plt.grid()
        if toShow:
            plt.show()


    def fitViaMatrixMethod(self, points):

        '''
        Fits a polynomial of degree len(points)-1 to the given data using the matrix method
        and plots the polynomial
        '''

        A, b = [], []
        xPoints = []
        yPoints = []
        low = 1000000
        high = -1000000

        # Creating the matrix A and the vector b
        for x, y in points:
            A.append([x**i for i in range(len(points))])
            b.append(y)
            low = min(low, x)
            high = max(high, x)
            xPoints.append(x)
            yPoints.append(y)

        coefficients = list(np.linalg.solve(A, b))
        p = Polynomial(coefficients)

        # display a plot with the given points and the computed polynomial
        plt.plot(xPoints, yPoints, "o", color='red')
        p.show(low, high, toShow=False)
        plt.title('Polynomial interpolation using matrix method ' + p.__getTitle())
        plt.show()

    def fitViaLagrangePoly(self, points):

        '''
        Fits a polynomial of degree len(points)-1 to the given data using lagrange method
        and plots the polynomial
        '''

        xPoints = []
        yPoints = []
        low = 1000000
        high = -1000000

        for x, y in points:
            low, high = min(low, x), max(high, x)
            xPoints.append(x)
            yPoints.append(y)

        p = Polynomial([0])

        # Finding the Lagrange polynomial
        for j in range(len(points)):

            nR, dR = Polynomial([1]), 1

            for i in range(len(points)):

                if i == j:
                    continue

                nR = nR * Polynomial([-xPoints[i], 1])
                dR = dR * (xPoints[j] - xPoints[i])

            p = p + ((yPoints[j]/dR) * nR)

        # display a plot with the given points and the computed polynomial
        plt.plot(xPoints, yPoints, "o", color='red')
        p.show(low, high, toShow=False)
        plt.title('Polynomial interpolation using lagrange method ' + p.__getTitle())
        plt.xlabel('x')
        plt.ylabel('f̃(x)')
        plt.show()

if __name__=='__main__':

    # p = Polynomial([1, 2, 3])
    # print(p[2])
    # p = Polynomial([])
    # p.fitViaMatrixMethod([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])
    # p.fitViaLagrangePoly([(1,-4), (0,1), (-1, 4), (2, 4), (3,1)])

    # p = Polynomial([1, -1, 1, -1])
    # p.show(-1, 2)

    # p = Polynomial([])
    # p.fitViaMatrixMethod([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])

    p = Polynomial([])
    p.fitViaLagrangePoly([(1,-4), (0,1), (-1, 4), (2, 4),(3,1)])