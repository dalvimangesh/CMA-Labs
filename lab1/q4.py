import random
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


class TextGenerator:

    # Initialize the prefix dictionary, total word counter, word to all tuple dictionary, and words list
    def __init__(self) -> None:
        self.prefixDic = dict()
        self.totalWords = '#ofTotalWords#' # using # at both end to make sure that this is not english word
        self.wordToAllTuple = dict()
        self.wordsList = list()


    # This function is used to process a given text file and create the prefix dictionary and wordToAllTuple
    def assimilateText(self, fileName):

        # Open the file
        file = open(fileName)
        # Read the data from the file
        data = file.read()
        # Split the data into individual words
        words = data.split()

        for i in range(0, len(words)-2):

            nextWord = words[i+2]
            curTuple = (words[i], words[i+1])

            # Create an empty list for the current word if it does not exist in the wordToAllTuple
            if curTuple[0] not in self.wordToAllTuple:
                self.wordToAllTuple[curTuple[0]] = list()

            self.wordToAllTuple[curTuple[0]].append(curTuple)
            self.wordsList.append(words[i])

            # Create an empty dictionary for the current tuple if it does not exist in the prefixDic
            if curTuple not in self.prefixDic:
                self.prefixDic[curTuple] = {self.totalWords: 0}

            # Increase the count of the next word
            if nextWord not in self.prefixDic[curTuple]:
                self.prefixDic[curTuple][nextWord] = 1
            else:
                self.prefixDic[curTuple][nextWord] += 1

            self.prefixDic[curTuple][self.totalWords] += 1

        self.wordsList.append(words[len(words) - 2])
        self.wordsList.append(words[len(words) - 1])

        # Normalize the counts for each next word to create a probability distribution
        for curTuple in self.prefixDic:
            sum = 0.0
            total = self.prefixDic[curTuple][self.totalWords]
            for word in self.prefixDic[curTuple]:
                if word == self.totalWords:
                    continue
                sum += self.prefixDic[curTuple][word] / total
                self.prefixDic[curTuple][word] = sum

                if word not in self.wordToAllTuple:
                    self.wordToAllTuple[word] = list()

            del self.prefixDic[curTuple][self.totalWords]


    '''
    This function is used to genearte text of given length and given start word
    if start word is not given it will select it randomly
    Number of words to be generated is mandatory argument
    '''
    @Check
    def generateText(self, num=None, word=None):

        if type(num) is not int:
            raise Exception('Number of words to be generated is mandatory argument')

        if (word is not None and (word not in self.wordToAllTuple)):
            raise Exception('Unable to produce text with the specified start word')

        # Function to get random word from all words
        def getRandomWord():
            return random.choice(self.wordsList)

        # function to get random tuple with given word as first element
        def getRandomTuple(startWith):
            return random.choice(self.wordToAllTuple[startWith])

        # function to select random word for given tuple
        def getWordFromPrefixDic(Tuple):

            randNumber = random.random()

            if Tuple not in self.prefixDic:
                return None

            for i in self.prefixDic[Tuple]:
                if self.prefixDic[Tuple][i] >= randNumber:
                    return i

        startWord = word # start word
        curTuple = None # to store current tuple , at start it is None
        generated = 0 # to store words in generated text
        answer = '' # to store generated text

        while True:

            # if start word is none so selecting one word randomly
            if startWord is None:
                startWord = getRandomWord()

            # if current tuple is None then finding random tuple with start word as first element
            if curTuple is None:
                curTuple = getRandomTuple(startWord)

                if curTuple is None:
                    answer += startWord
                    answer += ""
                    startWord = None
                    continue

                answer += curTuple[0]
                generated += 1
                if generated == num: # checking length
                    break
                answer += " "

                answer += curTuple[1]
                generated += 1
                if generated == num: # checking length
                    break
                answer += " "

            else:
                answer += curTuple[1]
                generated += 1
                if generated == num: # checking length
                    break
                answer += " "

            # we have tuple, so finding next word from PrefixDict
            newWord = getWordFromPrefixDic(curTuple)

            # if there is no next word then making start word as None and curTuple as None
            if newWord == None:
                startWord = None
                curTuple = None

            # updating the current tuple
            else:
                curTuple = (curTuple[1], newWord)

        print(answer)


if __name__ == '__main__':

    t = TextGenerator()
    t.assimilateText('sherlock.txt')
    t.generateText(50, 'London')