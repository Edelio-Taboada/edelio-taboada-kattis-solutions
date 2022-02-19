
t, s = map(str, input().split())

if t == "E":
    chars = []
    i = 0
    for char in s:
        if i == 0:
            chars.append(char)
            i+= 1
            chars.append(1)
        elif char == chars[i-2]:
            chars[i-1] = int(chars[i-1]) + 1
            i -= 1
        else:
            chars.append(char)
            i+= 1
            chars.append(1)
        i+= 1
    string = ""
    for char in chars:
        string = string + str(char)
    print(string)
else:
    string = ""
    i=0
    for x in range(int(len(s)/2)):
        for y in range(int(s[i+1])):
            string += s[i]
        i += 2
        continue
    print(string)
