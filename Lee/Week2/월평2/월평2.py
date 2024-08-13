import sys
sys.stdin = open('algo2_sample_in.txt', 'r')

from collections import deque
T = int(input())

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(road, m, n, start_goal):
    s_x, s_y = start_goal[:2]  # 시작 지점 x, y 값 변수 저장
    g_x, g_y = start_goal[2:]   # 도작 지점 x, y 값 변수 저장
    q = deque([(s_x, s_y)])     # 출발 지점
    
    # 방문 여부 저장 배열, 안간곳은 False로 저장
    visited = [[False]*m for _ in range(n)]
    
    # 시작 지점 True 표시
    visited[s_x][s_y] = True
    
    # 거리값 계산 배열
    distance = [[0]*m for _ in range(n)]

    # 이동 가능 여부 저장 변수
    move = True

    while q:
        x, y = q.popleft()

        # 이동 가능 여부
        # if move = True

        # dxy를 통한 위치 이동
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 > nx or nx > m or 0 > ny or ny > n:
                move = True
                continue

            # if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and distance[nx][ny] < distance[x][y] + 1 and move:

            # nx, ny가 배열 안의 인덱스이고 갔던 곳이 아니고 벽이 아닌 곳일때
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and distance[nx][ny] < distance[x][y] + 1 and road[nx][ny] != 1 and move:
                # print('move')
                q.append((nx, ny))
                visited[nx][ny] = True  # 간곳으로 저장
                distance[nx][ny] = distance[x][y] + 1   # 거리 값 계산

            # nx와 ny가 도착 지점에 왔을때
            if nx == g_x and ny == g_y:
                return distance[nx][ny]

    return -1   # 목적지에 멈출수 없을때


for test_case in range(1, T+1):
    # 입력 값을 할당 받음
    M, N = map(int, input().split())    # M, N 저장
    arr = [list(map(int, input().split())) for _ in range(M)]   # 네트워크
    start_goal = list(map(int, input().split()))    # 시작, 목적지 위치

    # 결과 출력 및 함수 호출
    print(f'#{test_case} {bfs(arr, M, N, start_goal)}')
