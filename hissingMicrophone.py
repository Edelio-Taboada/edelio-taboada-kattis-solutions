c=0
a=False
for each in input():
    if each is "s":
        c += 1
    else:
        c=0
    if c==2:
        print("hiss")
        a=True
        break
if not a:
    print("no hiss")
