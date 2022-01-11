import heapq

food_times = list(map(int, input().split()))
k = int(input())

# 전체 음식 먹는 시간이 주어진 시간보다 작거나 같다면 -1 출력
if sum(food_times) <= k:
    print("-1")

q = []
for i in range(len(food_times)):
    #낮은 음식 순서대로 자동 정렬 -> 음식 먹는 시간과 음식 라벨이 묶여서 힙 형태로 저장
    heapq.heappush(q, (food_times[i], i+1))

#먹는데 걸린 시간
sum = 0
#이전에 먹은 음식 시간
previous = 0

length = len(food_times)

#먹는데 걸린 시간 + (힙의 맨 첫 번째(즉 젤 소요시간 젤 작은 것) 음식 먹는데 걸리는 시간   - 이전에 먹은 음식 시간) * 현재 남아있는 음식의 개수가 k보다 작거나 같을때까지
#음식 먹는데 걸린 시간 - 이전에 먹은 음식 시간 빼는 이유 : 가장 작은 음식시간 빼면서 회전을 했기 때문
while sum + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    print(now)
    sum += (now - previous) * length
    length -= 1
    previous = now

result = sorted(q, key=lambda x: x[1])
print(result[(k - sum) % length][1])