import matplotlib.pyplot as plt
import math
import numpy as np

factOriginal = [0, 0]
fact = math.log(1)

for i in range(2, 1000001):
    fact = fact + math.log(i)
    factOriginal.append(fact)

factWithStirlingApprox = [-1000000]

for i in range(1, 1000001):
    val = (math.log(2*math.pi)/2) + ((math.log(i)) * (1/2 + i)) - (i * math.log(math.e))
    factWithStirlingApprox.append(val)

difference = []
for i in range(0,1000001):
    difference.append( factOriginal[i]-factWithStirlingApprox[i]  )



plt.plot(factOriginal,'r',label='log(n!)',linewidth = '1.5')

plt.plot(factWithStirlingApprox,'b:',label='log ( Stirling Approximation  for n)',linewidth = '3.5')

plt.xlabel('n')
plt.ylabel('log values')


plt.title('Stirlings approximation')
plt.legend(loc='best')
plt.grid()
plt.show()


plt.plot(difference,'r:' ,label=' log(n!) - log( Stirling Approximation for n ) ')
plt.ylim(-0.000001,0.000001)
plt.axhline( y = 0 ,color = 'blue', label = 'zero line')
plt.xlabel('n')
plt.legend(loc='best')
plt.grid()
plt.show()