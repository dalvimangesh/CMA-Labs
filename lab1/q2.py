from random import random
import matplotlib.pyplot as plt
import numpy as np
import sys

# Function to check for any exception in inputFunction
def Check(inputFunction):

    # Function to handle the exception
    def newFunction(ref, *arg, **kwargs):
        try:
            inputFunction(ref, *arg, **kwargs)
        except Exception as e:
            print(type(e))
            print(e)
            sys.exit(-1)

    return newFunction


# Dice class
class Dice:

    @Check
    def __init__(self, sides=6) -> None:

        # check if input is valid
        if ((type(sides) is not int) or sides < 4):
            raise Exception('Cannot construct the dice')
        self.numSides = sides
        self.cdf = list()
        commonProbability = 1 / self.numSides
        self.probabilityDistribution = [commonProbability] * sides
        self.cdf.append(commonProbability)
        for _ in range(self.numSides-1):
            self.cdf.append(self.cdf[-1] + commonProbability)

    # string representation of the dice and overloading print function
    def __str__(self) -> str:
        return f'Dice with {self.numSides} facesWithRandomNumber and probability distribution {{' + ", ".join(str(x) for x in self.probabilityDistribution) + '}'

    # function to set the probability distribution of the dice
    @Check
    def setProb(self, probabilityDistribution) -> None:
        '''
        checking
            1. input should be tuple
            2. len of the input should be equal to numSide
            3. sum of probabilities should be 1.00000 ( checking upto 5 precisions )
            4. All values should be non negaitve
        '''

        if ((type(probabilityDistribution) is not tuple)):
            raise Exception('Probability distribution should be in Tuple')

        if len(probabilityDistribution) != self.numSides or round(sum(probabilityDistribution), 5) != 1 or (min(probabilityDistribution) < 0):
            raise Exception('Invalid probability distribution')

        self.cdf[0] = probabilityDistribution[0]
        for i in range(1, len(probabilityDistribution)):
            self.cdf[i] = self.cdf[i-1] + probabilityDistribution[i]
        self.probabilityDistribution = list(probabilityDistribution)

    # function to roll the dice and plot the outcome
    @Check
    def roll(self, noOfThrows) -> None:

        # function to generate random number and get the index of the face based on the random number
        def getIndex(cdf):
            randomNumber = random()
            for ans, val in enumerate(cdf):
                if val >= randomNumber:
                    return ans

        # Empty list to store the count of each side
        facesWithRandomNumber = [0]*self.numSides
        facesWithActualNumber = [0]*self.numSides

        # generating the random number and increasing the frequency of the corresponding side
        for _ in range(noOfThrows):
            facesWithRandomNumber[getIndex(self.cdf)] += 1

        for i, probability in enumerate(self.probabilityDistribution):
            facesWithActualNumber[i] = int(round(probability*noOfThrows, 5))

        x = [(i+1) for i in range(self.numSides)]

        x_axis = np.arange(len(x))

        plt.bar(x_axis - 0.2, facesWithRandomNumber,0.4, label='random', color='red')
        plt.bar(x_axis + 0.2, facesWithActualNumber,0.4, label='actual', color='blue')

        plt.xticks(x_axis, x)
        plt.xlabel("sides")
        plt.ylabel("Occurrences")
        plt.title(f"Outcome of {noOfThrows} throws of a {self.numSides}-faced dice")
        plt.legend(loc='upper right')
        plt.show()


if __name__ == '__main__':

    d = Dice(6)
    d.setProb((0.2, 0.1, 0.4, 0.2, 0.05, 0.05))
    print(d)
    d.roll(1000)