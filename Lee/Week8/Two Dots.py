# # dfs로 탐색
# # 방향 3번 꺾고 처음 도착한곳하고 같으면
# # 시작점에 도착
#
# dxy = ((1,0), (-1,0), (0,1), (0,-1))
#
# def solution(cx, cy, count):
#     my_ch = arr[cx][cy]
#     visited[cx][cy] = True
#     global result
#
#     for dx, dy in dxy:
#         nx, ny = cx + dx, cy + dy
#
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#
#         # 범위 안에 있고 내 문자랑 다음 문자랑 같으면
#         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == my_ch:
#             if not visited[nx][ny]:
#                 solution(nx, ny, count + 1)
#                 visited[nx][ny] = False
#             elif visited[nx][ny] and sx == nx and sy == ny and count >= 3:
#                 result = "Yes"
#                 return
#
#         # visited[cx][cy] = False
#
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# result = "No"
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         sx, sy = i, j
#         if not visited[i][j]:
#             solution(i, j, 0)
#         if result == "Yes":
#             break
#
# print(result)
#

# 내가 푼건 탐색 중에 생긴 사이클은 찾지 못해서 시간이 오래 걸림
# 아래 방법은 visited로 방문 확인 / 이미 탐색한 곳은 시작점으로 안됨
# in_stack은 매번 solution 시작할때마다 초기화 돼서 시작되고 경로를 저장해감 / 굳이 시작점이 아니더라도 방향 꺾을때 해당 값이 내 경로에 있었으면 사이클 확인 완
dxy = ((1,0), (-1,0), (0,1), (0,-1))

def solution(cx, cy, px, py):
    global result
    my_ch = arr[cx][cy]
    visited[cx][cy] = True
    in_stack[cx][cy] = True

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        # 범위를 벗어난 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 다음 위치가 현재 문자와 동일한 경우
        if arr[nx][ny] == my_ch:
            # 방문하지 않은 경우, 계속 탐색
            if not visited[nx][ny]:
                if solution(nx, ny, cx, cy):  # 사이클이 발견되면 즉시 True 반환
                    return True

            # 부모 노드로 돌아가지 않고, 스택에 포함된 경로에서 사이클 발견 시
            elif in_stack[nx][ny] and (nx != px or ny != py):
                return True  # 사이클 발견됨

    # 스택에서 제거 (탐색 종료)
    in_stack[cx][cy] = False
    return False

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
in_stack = [[False] * M for _ in range(N)]
result = "No"

# 모든 지점에서 DFS 시작
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if solution(i, j, -1, -1):  # 시작점은 부모 노드가 없으므로 (-1, -1)로 설정
                result = "Yes"
                break
    if result == "Yes":
        break

print(result)

