from q1 import Polynomial


def getChebyshevPoly(n):

    '''
    function that uses the enhanced Polynomial class (developed in the last coding
    assignment) to compute the n th Chebyshev polynomial.
    '''

    try:
        if n < 0: raise Exception('n should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    T_0 = Polynomial([1]) # T1(x) = 1

    if n == 0: return T_0

    T_1 = Polynomial([0,1]) # T1(x) = x

    if n == 1: return T_1

    X = T_1

    # Generate the nth Chebyshev polynomial using the recurrence relation Tn+1(x) = 2*x*Tn(x) - Tn-1(x)
    for _ in range(2,n+1):
        T_N = 2 * X * T_1 - T_0
        T_0 = T_1
        T_1 = T_N

    # result
    return T_1

if __name__ == '__main__':

    print(getChebyshevPoly(n=2))
