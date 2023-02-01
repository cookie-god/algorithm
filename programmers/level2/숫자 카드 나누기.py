# 시간초과 30개
def solution1(arrayA, arrayB):
    answer = 0

    arrayA.sort()
    arrayB.sort()

    num = max(arrayA[0], arrayB[0])

    for i in range(2, num + 1):
        arrayAFlag = True
        arrayBFlag = True
        for item in arrayA:
            if item % i != 0:
                arrayAFlag = False
                break

        if arrayAFlag:
            for item in arrayB:
                if item % i == 0:
                    arrayBFlag = False
                    break
        else:
            for item in arrayB:
                if item % i != 0:
                    arrayBFlag = False
        if arrayAFlag and arrayBFlag:
            answer = i

        arrayAFlag = True
        arrayBFlag = True

        for item in arrayB:
            if item % i != 0:
                arrayBFlag = False
                break

        if arrayBFlag:
            for item in arrayA:
                if item % i == 0:
                    arrayAFlag = False
                    break
        else:
            for item in arrayA:
                if item % i != 0:
                    arrayAFlag = False
        if arrayAFlag and arrayBFlag:
            answer = i

    return answer

print(solution1([10, 17], [5, 20]))
print(solution1([10, 20], [5, 17]))
print(solution1([14, 35, 119], [18, 30, 102]))

# 시간초과 9개
def solution2(arrayA, arrayB):
    answer = 0

    arrayA.sort()
    arrayB.sort()

    num = max(arrayA[0], arrayB[0])

    for i in range(num, 0, -1):
        arrayAFlag = True
        arrayBFlag = True

        for item in arrayA:
            if item % i != 0:
                arrayAFlag = False
                break

        if arrayAFlag:
            for item in arrayB:
                if item % i == 0:
                    arrayBFlag = False
                    break

        if arrayAFlag and arrayBFlag:
            answer = i
            break

        arrayAFlag = True
        arrayBFlag = True

        for item in arrayB:
            if item % i != 0:
                arrayBFlag = False
                break

        if arrayBFlag:
            for item in arrayA:
                if item % i == 0:
                    arrayAFlag = False
                    break

        if arrayAFlag and arrayBFlag:
            answer = i
            break

    return answer

print(solution2([10, 17], [5, 20]))
print(solution2([10, 20], [5, 17]))
print(solution2([14, 35, 119], [18, 30, 102]))