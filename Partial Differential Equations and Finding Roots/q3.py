# Define a function to solve for the nth root of a number using the bisection method
def solveUsingBisectionMethod(n, a, epsilon):

    '''
    function that takes as its argument an integer n and two positive real numbers a and
    ε, then compute the n th root of a with an error tolerance of ε.
    '''

    # set the low and high initial bounds for the bisection method
    low = 0
    high = a

    while abs(high-low) > epsilon:

        mid = (low+high)/2

        nthPower = mid**n

        '''
        If the nth power of the midpoint is less than or equal to the target number,
        set the new lower bound to the midpoint
        '''
        if nthPower <= a:
            low = mid
        else:
            high = mid;

    # returns the average of the final upper and lower bounds
    return ( low + high ) / 2;


if __name__ == '__main__':

    print( solveUsingBisectionMethod( 2, 100 , 0.00001 ) )
