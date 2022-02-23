c = 0
n = input()
for each in list(map(int, input().split())):
    if each < 0:
        c+= 1
print(c)
