import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import romberg
from q1 import Polynomial

def getLegendrePoly(n) -> None:

    p = Polynomial([1])

    constantPoly = Polynomial([-1,0,1])

    for _ in range(n):
        p = p * constantPoly

    for _ in range(n):
        p = p.derivative()

    # Function to find the factorial of the input number
    factorial = lambda x : 1 if x == 0 else x * factorial(x-1)
    
    denominator = (2**n) * ( factorial(n) )

    return (1/denominator) * p

if __name__=='__main__':

    print(getLegendrePoly( n = 2 ))
