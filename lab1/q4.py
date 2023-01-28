import random
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


class TextGenerator:

    def __init__(self) -> None:
        self.prefixDic = dict()
        self.string = '#ofTotalWords#'
        self.wordToAllTuple = dict()
        self.wordsList = list()

    '''
    Some random function
    '''

    def assimilateText(self, fileName):

        file = open(fileName)
        data = file.read()
        words = data.split()

        for i in range(0, len(words)-2):

            nextWord = words[i+2]
            curTuple = (words[i], words[i+1])

            if curTuple[0] not in self.wordToAllTuple:
                self.wordToAllTuple[curTuple[0]] = list()

            self.wordToAllTuple[curTuple[0]].append(curTuple)
            self.wordsList.append(words[i])

            if curTuple not in self.prefixDic:
                self.prefixDic[curTuple] = {'#ofTotalWords': 0}

            if nextWord not in self.prefixDic[curTuple]:
                self.prefixDic[curTuple][nextWord] = 1
            else:
                self.prefixDic[curTuple][nextWord] += 1

            self.prefixDic[curTuple]['#ofTotalWords'] += 1

        self.wordsList.append(words[len(words) - 2])
        self.wordsList.append(words[len(words) - 1])

        for curTuple in self.prefixDic:
            sum = 0.0
            total = self.prefixDic[curTuple]['#ofTotalWords']
            for word in self.prefixDic[curTuple]:
                if word == '#ofTotalWords':
                    continue
                sum += self.prefixDic[curTuple][word] / total
                self.prefixDic[curTuple][word] = sum

                if word not in self.wordToAllTuple:
                    self.wordToAllTuple[word] = list()

            del self.prefixDic[curTuple]['#ofTotalWords']

    '''
    Some random function
    '''

    @Check
    def generateText(self, num=None, word=None):

        if type(num) is not int:
            raise Exception(
                'Number of words to be generated is mandatory argument')

        if (word is not None and (word not in self.wordToAllTuple)):
            raise Exception(
                'Unable to produce text with the specified start word')

        def getRandomWord():
            return random.choice(self.wordsList)

        def getRandomTuple(startWith):
            return random.choice(self.wordToAllTuple[startWith])

        def getWordFromPrefixDic(Tuple):

            randNumber = random.random()

            if Tuple not in self.prefixDic:
                return None

            for i in self.prefixDic[Tuple]:
                if self.prefixDic[Tuple][i] >= randNumber:
                    return i

        startWord = word
        curTuple = None
        generated = 0
        answer = ''

        while True:

            if startWord is None:
                startWord = getRandomWord()

            if curTuple is None:
                curTuple = getRandomTuple(startWord)
                answer += curTuple[0]
                generated += 1
                if generated == num:
                    break
                answer += " "
                
                answer += curTuple[1]
                generated += 1
                if generated == num:
                    break
                answer += " "

            else:
                answer += curTuple[1]
                generated += 1
                if generated == num:
                    break
                answer += " "

            newWord = getWordFromPrefixDic(curTuple)

            if newWord == None:
                startWord = None
                curTuple = None

            else:
                curTuple = (curTuple[1], newWord)


if __name__ == '__main__':

    t = TextGenerator()
    t.assimilateText('sherlock.txt')
    t.generateText(50, 'London')
