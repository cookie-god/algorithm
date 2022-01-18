S = input()

result = []
digit = 0
for data in S:
    if data.isalpha():
        result.append(data)
    else:
        digit += int(data)
result.sort()

if digit != 0:
    result.append(str(digit))

result = ''.join(result) #list -> string
print(result)