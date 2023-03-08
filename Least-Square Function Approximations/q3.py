from q1 import Polynomial

# function to get the nth Legendre polynomial
def getLegendrePoly(n) -> None:

    '''
    function that uses the enhanced Polynomial class (developed in the last coding
    assignment) to compute the n th Legendre polynomial.
    '''

    try:
        if n < 0: raise Exception('n should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    p = Polynomial([1]) # p as the constant polynomial 1

    constantPoly = Polynomial([-1,0,1]) # constant polynomial (x^2 - 1)

    # Multiplying p by the constant polynomial
    for _ in range(n):
        p = p * constantPoly

    # differentiate p n times
    for _ in range(n):
        p = p.derivative()

    # Function to find the factorial of the input number
    factorial = lambda x : 1 if x == 0 else x * factorial(x-1)
    
    denominator = (2**n) * ( factorial(n) )

    # Result
    return (1/denominator) * p

if __name__=='__main__':

    print(getLegendrePoly( n = 3 ))
