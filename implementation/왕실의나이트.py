def checkMove(x, y): #움직일 수 있는지 체크하는 함수
    if x < 1 or x > 8 or y < 1 or y > 8:
        return False
    return True

location = input()
column = ord(location[0])-ord('a')+1 #열
row = int(location[1]) #행

moveWay = [(-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2)] #움직일 수 있는 경우의 수
result = 0
for move in moveWay:
    if checkMove(column+move[0], row+move[1]):
        result += 1

print(result)