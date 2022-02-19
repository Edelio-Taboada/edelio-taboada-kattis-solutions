def factorial(int):
    for every in range(1, int):
        int = int * every
    return int


def last_digit(int):
    int = str(int)
    int = int[-1]
    return int


NumOfInts = int(input())
for every in range(NumOfInts):
    Input = int(input())
    print(last_digit(factorial(Input)))
