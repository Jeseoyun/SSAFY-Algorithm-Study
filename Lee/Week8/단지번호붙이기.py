# https://www.acmicpc.net/problem/2667 백준 단지번호붙이기
# BFS로 구역 찾고 개수 세고 끝나면 마지막에 센 개수를 결과 리스트에 넣어보자
from collections import deque

dxy = [(1,0), (-1,0), (0,1), (0,-1)]

def solution(s_x, s_y):
    if visited[s_x][s_y] > 0:
        return

    count = 1

    q = deque([(s_x, s_y, 0)])

    while q:
        c_x, c_y, c_c = q.popleft()
        for d_x, d_y in dxy:
            n_x, n_y = c_x + d_x, c_y + d_y

            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                continue

            if visited[n_x][n_y] > 0:
                continue

            if arr[n_x][n_y] == 0:
                continue

            visited[n_x][n_y] = 1
            q.append((n_x, n_y, count + 1))


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

for

