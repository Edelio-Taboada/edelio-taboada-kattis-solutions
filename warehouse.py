def getToy(e):
    return e[0]
def getCount(e):
    return e[1]
for every in range(int(input())):
    toys = 0
    dicto = {}
    for each in range(int(input())):
        listyy = input().split() 
        if listyy[0] in dicto:
            dicto[listyy[0]] += int(listyy[1])
        else:
            toys += 1
            dicto[listyy[0]] = int(listyy[1])
        
    listx = list(dicto.items())
    listx.sort(key=getToy)
    listx.sort(reverse=True, key=getCount)
    print(toys)
    for each in listx:
        print(str(each[0]) + " " + str(each[1]))
