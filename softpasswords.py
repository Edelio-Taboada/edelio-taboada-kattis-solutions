S = input()
P = input()


def prepending():
    testPassword = ""
    for every in range(0,10):
        testPassword = str(every) + P
        if testPassword == S:
            return(True)
    return(False)


def appending():
    testPassword = ""
    for every in range(0,10):
        testPassword = P + str(every)
        if testPassword == S:
            return(True)
    return(False)


if P.swapcase() == S or prepending() or appending() or P == S:
    print("Yes")
else:
    print("No")
