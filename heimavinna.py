#https://open.kattis.com/problems/heimavinna 
c = input().split(";")
co = 0
for each in c:
    if "-" in each:
        for every in range(list(map(int, each.split("-")))[0], list(map(int, each.split("-")))[1] + 1):
            co += 1
    else:
        co += 1
print(co)
