# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
import sys
sys.stdin = open('sample_input.txt', 'r')

# 이동 할 수 있는 방향
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# dfs는 gpt 선생님께서 하셨습니다.
def dfs(x, y, depth, chance):
    global result

    # 최대 등산로 길이 갱신
    result = max(result, depth)

    visited[x][y] = True

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        # 범위 넘으면 무시
        if not (0 <= nx < N and 0 <= ny < N):
            continue

        # 다음 위치의 높이가 현재 위치 보다 낮은 경우
        if arr[nx][ny] < arr[x][y]:
            dfs(nx, ny, depth + 1, chance)

        elif chance and arr[nx][ny] - K < arr[x][y] and not visited[nx][ny]:
            original_height = arr[nx][ny]
            arr[nx][ny] = arr[x][y] - 1
            dfs(nx, ny, depth + 1, False)
            arr[nx][ny] = original_height
    visited[x][y] = False

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 제일 큰 값을 갖고 있는 idx 저장 리스트
    max_idx = []

    # 리스트에서 가장 큰 값
    max_num = 0
    
    # 결과 저장
    result = 0

    # 방문 여부
    visited = [[False] * N for _ in range(N)]

    # 고점 찾기
    # 배열에서 제일 큰 값 찾기
    for i in range(0,len(arr)):
        if max(arr[i]) >= max_num:
            max_num = max(arr[i])
    
    # 제일 큰 값이 있는 idx 찾기
    for i in range(0, len(arr)):
        for j in range(0,len(arr)):
            if arr[i][j] >= max_num :
                max_idx.append([i,j])

    # 고점마다 출발
    for x, y in max_idx:
        # print(x,y)
        dfs(x, y, 1, True)

    print(f'#{test_case} {result}')