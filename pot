n = int(input())
sum = 0
for every in range(n):
    s = input()
    tempS = s
    s = int(s[:len(s)-1])
    tempS = int(tempS[len(tempS)-1:len(tempS)+1])
    sum += s**tempS
print(sum)
