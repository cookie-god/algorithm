import sys
from itertools import permutations

N = int(sys.stdin.readline())
# 순열을 이용해서 모든 경우의 수 넣음
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    test, s, b = map(int, sys.stdin.readline().split())
    # 한 자리씩 비교를 위해서 str로 변환
    test = list(str(test))
    remove_cnt = 0 # 배열에서 제거된 튜플 개수

    length = len(num)
    # num의 모든 숫자에 대해서 확인
    for i in range(length):
        # 스트라이크, 볼 개수 확인
        s_cnt = b_cnt = 0
        # 제거해야 다음 숫자 확인이 가능
        i -= remove_cnt

        # 3자리 확인
        for j in range(3):
            test[j] = int(test[j])
            # 숫자 하나가 num[i]에 존재한다면, 스트라이크 or 볼
            if test[j] in num[i]:
                # 같은 인덱스에 위치한다면
                if j == num[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        # 스트라이크나 볼의 개수가 같지 않다면 제거
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_cnt += 1

print(len(num))