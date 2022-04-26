c = float(input())
n = int(input())
t=0
for each in range(n):
    h,w = list(map(float, input().split()))
    t+= h*w*c
print("{:.8f}".format(t))
