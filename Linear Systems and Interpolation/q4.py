import numpy as np
import matplotlib.pyplot as plt

class Polynomial:

    def __init__(self, coefficients = None ) -> None:
        self.coefficients = coefficients
        self.degree = len(coefficients)-1 if coefficients is not None else 0

    def __str__(self) -> str:
        res = 'Coefficients of the polynomial are:\n' + " ".join(str(i) for i in self.coefficients)
        return res

    def __add__(self,p):
        tempCoeff = [0] * max( self.degree + 1,p.degree + 1 )
        
        for index,val in enumerate(self.coefficients):
            tempCoeff[index] += val

        for index,val in enumerate(p.coefficients):
            tempCoeff[index] += val

        return Polynomial(tempCoeff)

    def __sub__(self,p):

        tempCoeff = [0] * max( self.degree+1,p.degree+1 )
        
        for index,val in enumerate(self.coefficients):
            tempCoeff[index] += val

        for index,val in enumerate(p.coefficients):
            tempCoeff[index] -= val

        return Polynomial(tempCoeff)

    def __mul__(self, operand):
        tempCoeff = []
        if type(operand) is Polynomial:
            tempCoeff = self.__polyMul(operand)
        else:
            tempCoeff = self.__scalarMul(operand)
        return Polynomial(tempCoeff)

    def __rmul__(self, operand):
        return self.__mul__(operand)

    def __getitem__(self,x) -> float:
        res = 0
        for i,c in enumerate(self.coefficients):
            res += c * (x**i)
        return res

# Private

    def __scalarMul(self,scalar):
        tempCoeff = []
        for i in self.coefficients:
            tempCoeff.append(i*scalar)
        return tempCoeff
    
    def __polyMul(self,p):

        tempCoeff = dict()

        for coef1 in range(self.degree+1):
            for coef2 in range(p.degree+1):
                if coef1+coef2 not in tempCoeff:
                    tempCoeff[coef1+coef2] = 0
                tempCoeff[coef1+coef2] += self.coefficients[coef1] * p.coefficients[coef2]
        
        return [ val for _,val in tempCoeff.items() ]


    def __get_superscript(self,n: int) -> str:
        # Returns the superscript representation of a positive integer.
        superscript_digits = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
        # use str.translate to replace each digit with its corresponding superscript
        return str(n).translate(superscript_digits)

    def __getTitle(self):
        res = ""
        for power,value in enumerate(self.coefficients):
            if value == 0:
                continue
            if power == 0:
                res += str(round(value,2))
            elif power == 1:
                res += ('+' + str(round(value,2)) + 'x' ) if round(value,2) >= 0 else (str(round(value,2)) + 'x')
            else :
                res += ('+' + str(round(value,2)) + 'x' + self.__get_superscript(power)) if round(value,2) >= 0 else (str(round(value,2)) + 'x' + self.__get_superscript(power))
        if res == "" :res = str(0)
        return res
        
# Public

    def show(self,low,high,toShow=True):
        
        xPoints = list(np.linspace(low,high,100))
        yPoints = list(map(self.__getitem__,xPoints))

        plt.plot(xPoints,yPoints,color='blue')
        plt.xlabel('x')
        plt.ylabel('p(x)')
        plt.title("Plot of the polynomial " + self.__getTitle())
        plt.grid()
        if toShow: plt.show()

    def fitViaMatrixMethod(self,points):
        
        A,b = [],[]
        xPoints = []
        yPoints = []
        low = 1000000
        high = -1000000

        for x,y in points:
            A.append([x**i for i in range(len(points))])
            b.append(y)
            low = min(low,x)
            high = max(high,x)
            xPoints.append(x)
            yPoints.append(y)

        coefficients = list(np.linalg.solve(A,b))
        p = Polynomial(coefficients) 
        
        plt.plot(xPoints,yPoints,"o",color='red')
        p.show(low,high,toShow=False)
        plt.title('Polynomial interpolation using matrix method '+ p.__getTitle())
        plt.show()

    def fitViaLagrangePoly(self,points):

        xPoints = []
        yPoints = []
        low = 1000000
        high = -1000000

        for x,y in points:
            low,high = min(low,x),max(high,x)
            xPoints.append(x)
            yPoints.append(y)

        p = Polynomial([0])

        for j in range(len(points)):

            nR,dR = Polynomial([1]), 1

            for i in range(len(points)):

                if i == j:
                    continue
                
                nR = nR * Polynomial([-xPoints[i],1])
                dR = dR * ( xPoints[j] - xPoints[i] )

            p = p + ( (yPoints[j]/dR) * nR )

        plt.plot(xPoints,yPoints,"o",color='red')
        p.show(low,high,toShow=False)
        plt.title('Polynomial interpolation using matrix method '+ p.__getTitle())
        plt.xlabel('x')
        plt.ylabel('f̃(x)')
        plt.show()

p = Polynomial([])
p.fitViaLagrangePoly([(1,-4), (0,1), (-1, 4), (2, 4),(3,1)])
