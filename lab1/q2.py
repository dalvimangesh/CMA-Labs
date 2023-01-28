from random import random
import matplotlib.pyplot as plt
import numpy as np
import sys


def Check(method):

    def newFunction(ref, *arg, **kwargs):
        try:
            method(ref, *arg, **kwargs)
        except Exception as e:
            print(type(e))
            print(e)
            sys.exit(-1)

    return newFunction


class Dice:

    @Check
    def __init__(self, sides=6) -> None:

        if ((type(sides) is not int) or sides < 4):
            raise Exception('Cannot construct the dice')
        self.numSides = sides
        self.cdf = list()
        commonProbability = 1 / self.numSides
        self.probabilityDistribution = [commonProbability] * sides
        self.cdf.append(commonProbability)
        for _ in range(self.numSides-1):
            self.cdf.append(self.cdf[-1] + commonProbability)

    def __str__(self) -> str:
        return f'Dice with {self.numSides} facesWithRandomNumber and probability distribution {{' + ", ".join(str(x) for x in self.probabilityDistribution) + '}';

    @Check
    def setProb(self, probabilityDistribution) -> None:
        if ((type(probabilityDistribution) is not tuple)):
            raise Exception('Probability distribution should be in Tuple')

        if len(probabilityDistribution) != self.numSides or round(sum(probabilityDistribution),5) != 1 or (min(probabilityDistribution) < 0) :
            raise Exception('Invalid probability distribution')

        self.cdf[0] = probabilityDistribution[0]
        for i in range(1, len(probabilityDistribution)):
            self.cdf[i] = self.cdf[i-1] + probabilityDistribution[i]
        self.probabilityDistribution = list(probabilityDistribution)

    @Check
    def roll(self, noOfThrows) -> None:

        def getIndex(cdf, number):
            ans = 0
            for i in cdf:
                if i >= number:
                    return ans
                ans += 1
            return ans

        facesWithRandomNumber = [0]*self.numSides
        for _ in range(noOfThrows):
            randomNumber = random()
            facesWithRandomNumber[getIndex(self.cdf, randomNumber)] += 1

        facesWithActualNumber = [0]*self.numSides
        for i, probability in enumerate(self.probabilityDistribution):
            facesWithActualNumber[i] = int(probability*noOfThrows)

        print(facesWithRandomNumber)
        print(facesWithActualNumber)

        x = [(i+1) for i in range(self.numSides)]

        x_axis = np.arange(len(x))

        plt.bar(x_axis - 0.2, facesWithRandomNumber,0.4, label='random',color='red')
        plt.bar(x_axis + 0.2, facesWithActualNumber,0.4, label='actual',color='blue')

        plt.xticks(x_axis, x)
        plt.xlabel("sides")
        plt.ylabel("Occurrences")
        plt.title(f"Outcome of {noOfThrows} throws of a {self.numSides}-faced dice")
        plt.legend(loc='upper right')
        plt.show()


d = Dice(6)
d.setProb((0.2, 0.1, 0.4, 0.2, 0.05,0.05))
print(d)
d.roll(1000)
