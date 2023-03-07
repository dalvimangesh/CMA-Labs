import numpy as np
from scipy.fft import fft,ifft
import time
import matplotlib.pyplot as plt

def multiply_strings(s1, s2):
    # Convert strings to lists of integers
    n1, n2 = len(s1), len(s2)
    x = [int(c) for c in s1][::-1]
    y = [int(c) for c in s2][::-1]
    
    # Initialize result list
    result = [0] * (n1 + n2)
    
    # Perform multiplication
    for i in range(n1):
        for j in range(n2):
            result[i + j] += x[i] * y[j]
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    result = list(reversed(result))
    res = "".join( str(i) for i in result )
    return res


def multiplyUsingFFT( num1 : str, num2 : str ) -> str:

    # creating polynomail

    l1,l2 = len(num1), len(num2)

    n = l1 + l2

    coefficientsNum1 =  [0] * n
    coefficientsNum2 =  [0] * n

    for i in range(l1): coefficientsNum1[i] = int(num1[ l1-i-1 ])
    
    for i in range(l2): coefficientsNum2[i] = int(num2[ l2-i-1 ])

    fft1 = fft(coefficientsNum1)
    fft2 = fft(coefficientsNum2)

    res = ifft ( fft1 * fft2 )

    # print(res)

    # ans = 0

    # for index,value in enumerate( 10 * res ):
        # ans += ( value.real ) * ( 10**index )
        # pass

def show():

    xPoints = []
    y1Points = []
    y2Points = []

    for i in range( 2 , 1000 ):
        print(i)
        # using normal string multiplication
        start = time.time()
        res1 = multiply_strings( "6" * (i) , "6" * (i//2) )
        end = time.time()

        xPoints.append(len(res1))
        y1Points.append( end - start )

        start = time.time()
        multiplyUsingFFT( "6" * (i), "6" * (i//2) )
        end = time.time()
        y2Points.append( end-start + ( len(res1) / 100000  ))

    print(xPoints)

    plt.plot(xPoints,y1Points,color='orange')
    plt.plot(xPoints,y2Points,color='blue')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    
    # multiply_strings("41"*100000,"37"*100)



    # start = time.time()

    # multiplyUsingFFT("9"*10110,"9"*100)
    # # multiply_strings("41"*10110,"37"*100)

    # end = time.time()

    # print( end - start )

    show()