n = int(input())
arr = []
i = list(map(int, input().split()))
arr = list(range(i[0], i[1]+1))
for each in range(n - 1):
    i = list(map(int, input().split()))
    for c,every in enumerate(arr):
        if every < i[0]:
            arr[c] = -1
        elif every > i[1]:
            arr[c] = -1
if sum(arr) == (-1*len(arr)):
    print("edward is right")
else:
    print("gunilla has a point")
