import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from scipy.integrate import romberg, quad
from q1 import Polynomial
from q3 import getLegendrePoly
from q5 import getChebyshevPoly
from scipy.fft import fft,ifft


def multiplyUsingFFT( num1 : str, num2 : str ) -> str:

    # creating polynomail

    n = len(num1) + len(num2)

    coefficientsNum1 =  [0] * n
    coefficientsNum2 =  [0] * n

    for i in range(len(num1)): coefficientsNum1[i] = int(num1[i])
    for i in range(len(num2)): coefficientsNum2[i] = int(num2[i])

    fft1 = fft(coefficientsNum1)
    fft2 = fft(coefficientsNum2)

    res = ifft ( fft1 * fft2 )

    for i in res:
        print(i)



if __name__ == '__main__':

    multiplyUsingFFT("74","34")