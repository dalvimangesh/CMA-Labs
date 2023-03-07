import numpy as np
from scipy.fft import fft,ifft
import time

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


def add_big_strings(str1, str2):
    # Pad the strings with leading zeros to make them the same length
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        str2 = str2.zfill(len1)
    else:
        str1 = str1.zfill(len2)
    
    # Initialize variables for the result and carry
    result = []
    carry = 0
    
    # Add the digits from right to left
    for i in range(len(str1)-1, -1, -1):
        digit1 = int(str1[i])
        digit2 = int(str2[i])
        digit_sum = digit1 + digit2 + carry
        if digit_sum >= 10:
            carry = 1
            digit_sum -= 10
        else:
            carry = 0
        result.append(str(digit_sum))
    
    # Add any remaining carry to the leftmost digit
    if carry > 0:
        result.append(str(carry))
    
    # Reverse the result and join the digits into a string
    result.reverse()
    str_result = ''.join(result)
    
    return str_result

def getPowerOfTen(index):
    res = "1"
    for _ in range(index):
        res = res + "0"
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

    print(res)

    ans = "0"

    for index,value in enumerate(res):
        ans =  add_big_strings ( ans ,  multiply_strings(str(int(value.real)) , getPowerOfTen ( index )))

    # print(ans)

if __name__ == '__main__':
    
    # multiply_strings("41"*100000,"37"*100)

    # print(getPowerOfTen(100000))

    multiplyUsingFFT("41"*10,"37"*10)
