n,w,h = map(int, input().split())
#pythagorean theorem to see if it fits
tot = ((w**2)+(h**2))**0.5
for i in range(n):
    if int(input()) <= tot:
        print("DA")
    else:
        print("NE")
