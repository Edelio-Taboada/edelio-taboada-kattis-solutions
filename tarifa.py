megabytesMonthly = int(input())
megabyteCount = 0
months = int(input())
monthlyUsage = []
for every in range(months):
    megabyteCount += megabytesMonthly
    megabyteCount -= int(input())

print(megabyteCount + megabytesMonthly)
