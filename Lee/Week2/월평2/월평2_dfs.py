import sys
sys.stdin = open('algo2_sample_in.txt', 'r')


def dfs(x, y, distance):
    global result

    # 방문처리
    visited[x][y] = True

    # 최단 거리 결과값 저장
    # 도착지점 도착 시 결과 반환
    if x == g_x and y == g_y:
        result = min(result, distance)
    
    # 도착 못하면 -1로 반환해야댐


    for dx, dy in dxy:
        nx, ny = dx + x, dy+ y
    
        # 벽에 부딪히면 방향 전환
        if not (0 <= nx < M and 0 <= ny < N) or arr[nx][ny] == 1:
            # conflict = True
            # 4번 부딪히면 -1로 반환할까?
            continue
        
        # 방문 안한 곳이면 이동
        if not visited[nx][ny]:
            dfs(nx, ny, distance + 1)
    
    visited[x][y] = False



T = int(input())

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for test_case in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start_goal = list(map(int, input().split()))

    # 시작, 도착 좌표
    s_x, s_y, g_x, g_y = start_goal

    # 결과값
    result = 9999

    # 방문여부
    visited = [[False] * M for _ in range(N)]

    dfs(s_x, s_y, 0)
    print(result)