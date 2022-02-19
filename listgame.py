import math
input = int(input())
currentNumber = input
factors = []
factorsFixed = []
prime = False
pointCounter = 0

def findFactor(x):
    global prime
    factor_count = 0
    for every in range(2, int(math.sqrt(x)) + 1):
        if x / every == int(x/every):
            factor_count += 1
            return every
    if factor_count == 0:
        prime = True
        return int(currentNumber)


while prime is False:
    factors.append(findFactor(currentNumber))
    currentNumber = currentNumber / int(factors[-1])


for every in factors:
    pointCounter += 1

print(pointCounter)
