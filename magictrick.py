def double():
    i = input()
    for each in i:
        c = 0
        for every in i:
            if each == every:
                c+=1
        if c > 1:
            return 0
    return 1
print(double())
