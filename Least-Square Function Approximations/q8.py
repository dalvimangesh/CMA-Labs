from scipy.fft import fft,ifft
import time
import matplotlib.pyplot as plt

# function to multiply to two number of string form
def multiplyStrings(s1, s2):

    try:
        if type(s1) is not str or type(s2) is not str:
            raise Exception('Numbers should be in form of string')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    try:
        if s1[0]=='-' or s2[0]=='-':
            raise Exception('Numbers should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)
    

    # convert strings to lists of int
    n1, n2 = len(s1), len(s2)
    x = [int(c) for c in s1][::-1]
    y = [int(c) for c in s2][::-1]
    
    # initialize result list
    result = [0] * (n1 + n2)
    
    # perform multiplication
    for i in range(n1):
        for j in range(n2):
            result[i + j] += x[i] * y[j]
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    result = list(reversed(result))
    res = "".join( str(i) for i in result )
    return res

# function, with time complexity of O(n log n), to multiply two large n-digit integers.
def multiplyUsingFFT( num1 : str, num2 : str , isShow = False) -> str:

    try:
        if type(num1) is not str or type(num2) is not str:
            raise Exception('Numbers should be in form of string')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    try:
        if num1[0]=='-' or num2[0]=='-':
            raise Exception('Numbers should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    l1,l2 = len(num1), len(num2)

    n = l1 + l2

    coefficientsNum1 =  [0] * n
    coefficientsNum2 =  [0] * n

    for i in range(l1): coefficientsNum1[i] = int(num1[ l1-i-1 ])
    
    for i in range(l2): coefficientsNum2[i] = int(num2[ l2-i-1 ])

    # apply the FFT to the coefficient arrays
    fft1 = fft(coefficientsNum1)
    fft2 = fft(coefficientsNum2)

    # Multiply the two polynomials in the frequency domain
    res = ifft ( fft1 * fft2 )

    if isShow == True: return

    ans = 0

    # convert the resulting polynomial back to a string representation of the result
    for index,value in enumerate( res ):
        ans += round( value.real ) * ( 10**index )
        
    return str(ans)

def show():

    xPoints = []
    y1Points = []
    y2Points = []

    for i in range( 2 , 2000, 30 ):
        print(i)
        # using normal string multiplication
        start = time.time()
        res1 = multiplyStrings( "6" * (i) , "6" * (i//2) )
        end = time.time()

        xPoints.append(len(res1))
        y1Points.append( end - start )

        start = time.time()
        multiplyUsingFFT( "6" * (i), "6" * (i//2), isShow = True )
        end = time.time()
        # assuming that function after ifft takes 2 * ( len(res1) / 100000  ) time final calculations
        y2Points.append( end-start + 2 * ( len(res1) / 100000  )) 

    plt.plot(xPoints,y1Points,color='orange',label='normal multiplication')
    plt.plot(xPoints,y2Points,color='blue',label='fft')
    plt.title('time vs number of digits in product')
    plt.xlabel('number of digits in product')
    plt.ylabel('time')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    
    num1 = "22315312234231444444444444444444444444444213421431342414"
    num2 = "31231223412344444444444443444444444444443241124331325523"

    print('Product using normal multiplication : ' , multiplyStrings(num1,num2))
    print('Product using normal fft :            ' , multiplyUsingFFT(num1,num2))

    # show()