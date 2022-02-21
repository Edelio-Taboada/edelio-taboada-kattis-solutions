vert = 0
for i in range(int(input())+1):
    if i == 0:
        vert = 2
    else:
        vert += vert-1
print(vert**2)
