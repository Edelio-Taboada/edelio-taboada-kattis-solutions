n, m = map(int, input().split())
tot = 0
for i in range(m):
    tot += int(input())
print(str((tot+(-3)*(n-m))/n) + " " + str((tot+3*(n-m))/n))
