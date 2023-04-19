

def solveUsingBisectionMethod(n, a, epsilon):

    low = 0
    high = a

    while abs(high-low) > epsilon:

        mid = (low+high)/2

        nthPower = mid**n

        if nthPower <= a:
            low = mid
        else:
            high = mid;

    return ( low + high ) / 2;


if __name__ == '__main__':

    print( solveUsingBisectionMethod( 2, 100 , 0.00001 ) )
