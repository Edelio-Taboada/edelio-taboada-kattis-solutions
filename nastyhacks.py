for every in range(int(input())):
    i = list(map(int, input().split()))
    if i[1] - i[2] < i[0]:
        print("do not advertise")
    elif i[1] - i[2] == i[0]:
        print("does not matter")
    else:
        print("advertise")
