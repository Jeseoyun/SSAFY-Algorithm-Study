# # https://www.acmicpc.net/problem/7562 백준 나이트의 이동
#
#
# # 나이트는 본인 위치에서 상하좌우 2칸 이동 후 좌우 이동
# # dfs로 해보자~
# # 도착지점 도착시 걸린 횟수 갱신(최소값) return
# # 걸린횟수가 최솟값 보다 크면 return
#
# def dfs(x, y, visited, depth):
#     global result
#
#     # 최솟값 보다 크면 종료
#     if depth >= result:
#         return
#
#     # 도착지점 도착하고 result보다 depth가 작으면 갱신 및 종료
#     if x == goal_position[0] and y == goal_position[1]:
#         if depth < result:
#             result = depth
#         return
#
#     # 이동
#     for dx, dy in dxy:
#         nx, ny = x + dx, y + dy
#
#         # 다음 위치가 board 범위 밖이면 다음으로
#         if 0 > nx or nx >= N or 0 > ny or ny >= N:
#             continue
#
#         # 다음 장소가 방문 안한 곳이면 이동
#         if not visited[nx][ny]:
#             visited[nx][ny] = True
#             dfs(nx, ny, visited, depth + 1)
#             visited[nx][ny] = False
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     knight_position = list(map(int, input().split()))
#     x, y = knight_position[0], knight_position[1]
#     goal_position = list(map(int, input().split()))
#
#     # 이동 리스트
#     dxy = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [-1, -2], [1, -2]]
#
#     # 체스 판
#     board = [[0] * N for _ in range(N)]
#
#     visited = [[False] * N for _ in range(N)]
#     visited[x][y] = True
#     result = float('INF')
#     dfs(x, y, visited, 0)
#
#     print(result)
#

# ㅠㅠ DFS 재귀호출 에러로 BFS로 해야함
# BFS
from collections import deque

def bfs(x, y):
    # 나이트 이동 경로 리스트
    dxy = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [-1, -2], [1, -2]]

    visited = [[-1] * N for _ in range(N)]
    q  = deque([(x, y, 0)])

    while q:
        cx, cy, depth = q.popleft()

        if cx == goal_position[0] and cy == goal_position[1]:
            return depth

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] > -1: continue
            visited[nx][ny] = depth + 1
            q.append((nx, ny, depth + 1))

T = int(input())
for tc in range(T):
    N = int(input())
    knight_position = list(map(int, input().split()))
    x, y = knight_position[0], knight_position[1]
    goal_position = list(map(int, input().split()))

    if x == goal_position[0] and y == goal_position[1]:
        print(0)
    else:
        print(bfs(x, y))

