import random


numberOfBits = 64


def initalPermutation(data):
    #print(data)
    arrayOfNumbers = [i for i in range(0, numberOfBits)]
    arrayOfNumbersShuffled = [i for i in range(0, numberOfBits)]
    random.shuffle(arrayOfNumbersShuffled)
    newData = ""
    for i in range(0, numberOfBits):
        newData = newData + data[arrayOfNumbersShuffled[i]]
    return newData, arrayOfNumbers, arrayOfNumbersShuffled


def finalPermutation(newData, arrayOfNumbersShuffled):
    revData = [i for i in range(0, numberOfBits)]

    for i in range(0, numberOfBits):
        temp = arrayOfNumbersShuffled[i]
        revData[temp] = newData[i]
    revData2 = "".join(revData)
    return revData2


newData, arrayOfNumbers, arrayOfNumbersShuffled = initalPermutation(
    "dsajdhashjdhjashdjashqwewqjeqejnadbdasbwqieiqwewnnmsadnma3232sss")
revData2 = finalPermutation(newData, arrayOfNumbersShuffled)


#print(newData)
#print(arrayOfNumbers)
#print(arrayOfNumbersShuffled)
#print(revData2)
