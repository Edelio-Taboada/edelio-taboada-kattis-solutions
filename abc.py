#Takes in the first line of input, separates the strings by space, maps them onto the type int, and converts it back into a list which now contains ints
nums = list(map(int, input().split()))
dicto = {}
dicto["A"] = min(nums)
dicto["C"] = max(nums)
for x in nums:
    if x>dicto["A"] and x<dicto["C"]:
        dicto["B"]=x
out = ""
#iterates through each character in the second line string, but it
for ord in input():
    out += str(dicto[ord]) + " "
print(out)
