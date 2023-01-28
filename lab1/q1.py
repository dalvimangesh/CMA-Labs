import matplotlib.pyplot as plt
import math
import numpy as np

inf = 1000000 # Assuming 1000000 as -infinity

def findLogActualFactorials(n):

    # storing the log of actual factorials
    ActuralFactorials = [0, 0]
    fact = math.log(1)

    for i in range(2, n+1):
        fact = fact + math.log(i)
        ActuralFactorials.append(fact)

    return ActuralFactorials


def findLogWithStirling(n):

    # storing the log of Stirling Approximation
    logStirling = [-inf]  

    def findLogStirling(num) -> float:
        val = (math.log(2*math.pi)/2) + ((math.log(i))
                                         * (1/2 + i)) - (i * math.log(math.e))
        return val

    for i in range(1, n+1):
        val = findLogStirling(i)
        logStirling.append(val)

    return logStirling




def findDiff(list1, list2):
    n = len(list1)
    difference = []
    for i in range(0, n):
        difference.append(list1[i]-list2[i])
    return difference


if __name__ == '__main__':

    noOfExpt = 1000000

    ActuralFactorials = findLogActualFactorials(noOfExpt)
    logStirling = findLogWithStirling(noOfExpt)

    # storing differences in actual and Stirling Approximation
    difference = findDiff(ActuralFactorials, logStirling)

    plt.plot(ActuralFactorials, 'r', label='log(n!)', linewidth='1.5')
    plt.plot(logStirling, 'b:',
             label='log ( Stirling Approximation  for n)', linewidth='3.5')
    plt.xlabel('n')
    plt.ylabel('log values')
    plt.title('Stirlings approximation')
    plt.legend(loc='best')
    plt.grid()
    plt.show()

    plt.plot(difference, color='tab:red',
             label=' log(n!) - log( Stirling Approximation for n ) ', linestyle='solid')
    plt.ylim(-0.000003, 0.000003)
    plt.axhline(y=0, color='tab:blue', label='zero line')
    plt.xlabel('n')
    plt.legend(loc='best')
    plt.title('Differences in actual and Stirling Approximation')
    plt.grid()
    plt.show()
