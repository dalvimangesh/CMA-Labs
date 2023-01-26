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

# difference = []
# for i in range(0,1000001):
#     difference.append(factOriginal[i]-factWithStirlingApprox[i])


plt.plot(factOriginal,'r',label='Original Factorial',linewidth = '1.5')

plt.plot(factWithStirlingApprox,'b:',label='Stirling Approximation',linewidth = '3.5')

# plt.plot([0]*(len(factOriginal)+len(factOriginal)),range(-1000001,1000001))
# plt.plot(range(0,1000001),[0]*len(factOriginal))

# plt.scatter(difference,'g--')

plt.xlabel('integers')
plt.ylabel('factorials')


plt.title('Stirlings approximation')
plt.legend(loc='best')
plt.show()
