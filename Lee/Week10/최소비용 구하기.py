# https://www.acmicpc.net/problem/1916 최소비용 구하기
# dfs 처럼 타고타고 들어가보자
# 끝까지 타고 갔는데 현재 나온 값 보다 크면 백트래킹
# 목표 도시에 도착하면 return
## !! DFS 시간 초과 !!

from collections import defaultdict

# goal_start city, ,, 약어
def solution(c_c, value_sum, visited):
    global result

    # 이동 간 result 보다 큰 경로면
    if value_sum >= result:
        return

    # 목표 도시 도착
    if c_c == end_goal_city:
        result = value_sum
        return

    visited[c_c] = True

    for n_c, value in city_dict[c_c]:
        if not visited[n_c]:
            solution(n_c, value_sum + value, visited)

    visited[c_c] = False

N = int(input())
M = int(input())
result = float('inf')

city_dict = defaultdict(list)

visited = [False] * (N + 1)

# key : 시작 도시, value : [도착 도시, 비용]
for _ in range(M):
    start_city, end_city, value = map(int, input().split())
    city_dict[start_city].append([end_city, value])

# 목표 출발, 도착 도시
start_goal_city, end_goal_city = map(int, input().split())

solution(start_goal_city, 0, visited)

print(result)