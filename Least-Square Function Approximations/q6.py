import math
from scipy.integrate import quad # using quad to avoid divide by zero error
from q5 import getChebyshevPoly


def verifyChebyshevPoly(n=5):

    '''
    function to compute the first 5 Chebyshev polynomials and numerically demonstrate that they 
    are orthogonal with respect the weight function w(x) =  sqrt(1/ 1 - x^2) in the interval [-1, 1]
    '''

    try:
        if n < 0: raise Exception('n should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    chebyshev = [] # create an empty list to store the first n Chebyshev polynomials

    for i in range(n):
        chebyshev.append(getChebyshevPoly(i))

    w = lambda x : 1 / math.sqrt(1 - x**2)

    res = [] #  list to store the results of the numerical integration
    a = -1
    b = 1

    ''' each pair of Chebyshev polynomials i and j,  calculate their product 
    with the weight function and numerically integrate it using the romberg integration method '''
    for i in range(n):
        for j in range(n):
            def curFun(x): return w(x) * chebyshev[i][x] * chebyshev[j][x]
            cj = quad( func = curFun, a=a, b=b )[0]
            if round(cj, 2) == 0:
                cj = 0
            res.append([(i, j), round(cj, 2)])

    # Result
    for e in res:
        print(e)


if __name__ == '__main__':

    verifyChebyshevPoly()
