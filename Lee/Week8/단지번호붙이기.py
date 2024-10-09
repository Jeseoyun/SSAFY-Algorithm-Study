# https://www.acmicpc.net/problem/2667 백준 단지번호붙이기
# BFS로 구역 찾고 개수 세고 끝나면 마지막에 센 개수를 결과 리스트에 넣어보자
from collections import deque

dxy = [(1,0), (-1,0), (0,1), (0,-1)]

def solution(s_x, s_y):
    if visited[s_x][s_y] > 0:
        return -1

    count = 1

    q = deque([(s_x, s_y, count)])
    visited[s_x][s_y] = 1

    while q:
        c_x, c_y, c_c = q.popleft()
        for d_x, d_y in dxy:
            n_x, n_y = c_x + d_x, c_y + d_y

            # 범위 넘으면
            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                continue

            # 사람 사는 곳이 아니면
            if arr[n_x][n_y] == 0:
                continue

            # 이미 탐색한 곳이면
            if visited[n_x][n_y] > 0:
                continue

            visited[n_x][n_y] = 1
            count += 1
            q.append((n_x, n_y, count))

    return count


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
result = []

# 1인 곳마다 solution 함수 실행
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            danG = solution(i, j)
            # 단지 계산 했으면 결과에 저장
            if danG > 0:
                result.append(danG)

result.sort()
# print(visited)
if len(result) == 0:
    print(0)
else:
    print(len(result))
    for idx, k in enumerate(result):
        if idx == len(result):
            print(k, end='')
        else:
            print(k)