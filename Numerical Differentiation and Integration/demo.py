def derivative(self):
    dv = []
        # dv will store the coefficients of the derivative polynomial
        # coefficient will change as : a.xⁿ -> a.n.x⁽ⁿ⁻¹⁾
        # 0 th degree coefficient of the polynomial is omitted in its derivative
    for i in range(1, len(self.coeff)):
        d = i*self.coeff[i]
        dv.append(d)
    return dv

    """
        Calculates the coefficients of the integral polynomial
    """
def integral(self):
        # 0th degree coefficient of this integral polynomial would be 0
        # and rest will change according to integration rule
    self.integralPoly = [0]
    for i in range(len(self.coeff)):
        v = self.coeff[i]/(i+1)
        self.integralPoly.append(v)

    """
        Returns the integral value at the given x
    """
def integralValue(self, x):
    ans = 0
    # finds integration value by substituting given x in the integral polynomial
    for i in range(len(self.integralPoly)):
        ans += self.integralPoly[i] * (x**i)
    return ans

    """
        Returns area under the curve for in the given interval
    """
def area(self, a, b):
    if not isinstance(a, (float, int)) or not isinstance(b,(float,int)):
        raise Exception("Invalid type for interval given")

    if a > b:
        raise Exception("Invalid interval input: a should be less than b")
        # creates integral polynomial
    self.integral()
        # then finds integration value and thus area
    return (self.integralValue(b) - self.integralValue(a))
