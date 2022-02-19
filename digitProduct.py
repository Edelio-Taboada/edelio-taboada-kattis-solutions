list = []
currentNumber = input()
iterationCounter = 0

def digitProduct(x):
    productTracker = 1
    for every in str(x):
        if int(every) > 0:
            productTracker = productTracker * int(every)
    return(productTracker)

while len(str(currentNumber)) > 1 or iterationCounter == 0:
    currentNumber = digitProduct(currentNumber)
    iterationCounter += 1

print(currentNumber)
