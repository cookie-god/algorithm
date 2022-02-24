N, start, end = map(int, input().split())
count = 0 # 정답

while start != end: #결국 같은 번호가 됨
    start -= start//2 #1번은 다음에 1번, 3번은 다음에 2번이 되는 구조
    end -= end//2 #1번은 다음에 1번, 3번은 다음에 2번이 되는 구조
    count += 1 #카운트 증가

print(count)