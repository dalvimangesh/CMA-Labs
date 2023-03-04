import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from scipy.integrate import romberg
from q1 import Polynomial
from q3 import getLegendrePoly


def getChebyshevPoly(n):

    T_0 = Polynomial([1]) # T1(x) = 1

    if n == 0: return T_0

    T_1 = Polynomial([0,1]) # T1(x) = x

    if n == 1: return T_1

    X = T_1

    for _ in range(2,n+1):
        T_N = 2 * X * T_1 - T_0
        T_0 = T_1
        T_1 = T_N

    return T_1


if __name__ == '__main__':

    print(getChebyshevPoly(n=2))
