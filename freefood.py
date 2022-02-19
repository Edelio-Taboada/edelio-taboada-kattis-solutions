NumEvents = int(input())
ListList = []
ListDays = []
TrueListDays = []
i = 0
DaysCount = 0
for i in range(NumEvents):
    Input = input()
    ListList.append(Input.split())

for every in ListList:
    for integers in range(int(every[0]), int(every[1])):
        ListDays.append(integers)
    ListDays.append(int(every[1]))

ListDays = set(ListDays)

for every in ListDays:
    DaysCount += 1

print(DaysCount)
