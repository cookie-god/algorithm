import sys

x, y = map(int, sys.stdin.readline().split())
result = 0

for i in range(1, x):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        result += 31
    elif i == 2:
        result += 28
    else:
        result += 30

result += y

if result % 7 == 1:
    print("MON")
elif result % 7 == 2:
    print("TUE")
elif result % 7 == 3:
    print("WED")
elif result % 7 == 4:
    print("THU")
elif result % 7 == 5:
    print("FRI")
elif result % 7 == 6:
    print("SAT")
else:
    print("SUN")