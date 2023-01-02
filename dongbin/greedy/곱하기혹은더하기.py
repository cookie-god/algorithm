data = input()

result = 0
for i in range(len(data)):
    if result == 0:
        result += int(data[i])
    elif data[i] == '0' or data[i] == '1':
        result += int(data[i])
    else:
        result *= int(data[i])

print(result)