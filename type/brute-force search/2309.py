import sys

heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline()))

sum = sum(heights)
x = 0
y = 0
answer = False

for i in range(8):
    for j in range(i+1, 9):
        if (sum - (heights[i] + heights[j]) == 100):
            x = heights[i]
            y = heights[j]
            answer = True
            break
    if answer == True:
        break

heights.remove(x)
heights.remove(y)
heights.sort()

for height in heights:
    print(height)
