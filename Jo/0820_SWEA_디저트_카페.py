# import sys
# sys.stdin = open("dessert_input.txt", "r")

#대각선 방향으로 4방향을 잡는다
dij = [(1, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

def dfs(n, current_i, current_j, visited):
    global answer

    # 네 번 꺾게 되면 그때부터는 뱅그르르 돌아버림. 멈춰주자
    .
    if n > 3:
        return
    # 세 번 꺾으면 사각이 완성되고 시작점과 끝점이 같다면 사각형이 완성됨
    if nn == 3 ad start_i == current_i and start_j == current_j:
        # 기존의 answer값과 비교하여 값 갱신
        answer = max(answer, len(visited))
        return

    # 대각으로 직진을 하거나 왼쪽으로 꺾어버린다
    for k in range(n, n + 2):
        next_i, next_j = current_i + dij[k][0], current_j + dij[k][1]
        if 0 <= next_i < N and 0 <= next_j < N and region[next_i][next_j] not in visited:
            visited.append(region[next_i][next_j])
            dfs(k, next_i, next_j, visited)
            visited.pop()

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    # 모든 점에 대하여 dfs 적용
    for start_i in range(N):
        for start_j in range(N):
            dfs(0, start_i, start_j, [])
    print(f'#{test_case} {answer}')