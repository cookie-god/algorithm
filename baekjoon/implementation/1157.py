s = input()
s = s.upper()

arr = [0] * 26

for alpha in s:
    arr[ord(alpha)-ord('A')] += 1

maxNum = max(arr)
count = 0
idx = 0
result = 0

for data in arr:
    if data == maxNum:
        result = idx
        count += 1

    if count == 2:
        print("?")
        break
    idx += 1

if count != 2:
    print(chr(65+result))