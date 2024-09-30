import sys
sys.stdin = open("sample_input.txt", "r")

#4방향 순회를 위한 dx,dy 선언. 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 거리 계산을 위한 dfs 함수 구현. (행 열 좌표, k값, 거리)를 매개변수로
def find_the_longest(row, col, K, length):
    global result

    #기존 값보다 length가 길다면 최댓값 갱신
    if length > result:
        result = length

    #현재 위치 방문 처리
    visited[row][col] = True

    #4방향 순회
    for x, y in zip(dx, dy):
        nx = row + x
        ny = col + y

        # nx, ny가 road 범위 내에 있고 방문하지 않았을 때 적용
        if 0<= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 다음 이동하는 값이 현재 값보다 작다면 그대로 dfs함수 실행
            if road[nx][ny] < road[row][col]:
                find_the_longest(nx, ny, K, length + 1)
            # 다음 이동하는 값이 현재 값과 같거나 크다면?
            elif (road[nx][ny] == road[row][col] and K) or (road[nx][ny] > road[row][col] and K > (road[nx][ny] - road[row][col])):
                temp = road[nx][ny]
                #다음 점을 현재 점보다 1만 작게 만들면 됨
                road[nx][ny] = road[row][col] - 1
                find_the_longest(nx, ny, 0, length + 1)
                #원상복귀
                road[nx][ny] = temp

    # 다른 시작점부터의 루트가 해당 지점을 탐색할 수 있도록 방문 처리 해제
    visited[row][col] = False

T = int(input())

for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    road = [list(map(int, input().split())) for _ in range(N)]

    # 최댓값과 방문 처리용 visited table
    result = 0
    visited = [[0] * N for _ in range(N)]

    # road 내 최댓값 찾기
    max_value = 0
    lst = []
    for i in range(len(road)):
        lst.append(max(road[i]))
    max_value = max(lst)

    # 해당 좌표가 최댓값일 때 함수 실행
    for i in range(N):
        for j in range(N):
            if road[i][j] == max_value:
                find_the_longest(i, j, K, 1)

    print(f'#{test_case} {result}')
