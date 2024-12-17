from functools import reduce
def maximumAverage(numbers, range):
    startIndex = 0
    lengthOfNumbers = len(numbers)
    listofAverages = []

    while startIndex < lengthOfNumbers - range + 1:
        numbersToAdd = numbers[startIndex: startIndex + range]
        average = reduce(lambda a, b: a + b, numbersToAdd) / range
        listofAverages.append(average)
        startIndex += 1
        print("numbers to add", numbersToAdd,"average", average)

    return max(listofAverages)       