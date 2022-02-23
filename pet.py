c = [-1, -1]

for each in range(5):
    i = sum(list(map(int, input().split())))
    if i > c[1]:
    
        c[0] = each + 1
        c[1] = i
print(str(c[0]) + " " + str(c[1]))   
