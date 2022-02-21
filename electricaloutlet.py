n = int(input())
for i in range(n):
    li = list(map(int, input().split()))
    total = 0
    for c,j in enumerate(li):
        if c != 0:
            total -= 1
            total += j
    print(total + 1)
