import sys
sys.stdin = open("dessert_input.txt", "r")

dij = [(1, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

def dfs(n, current_i, current_j, visited):
    global answer

    if n > 3:
        return
    if n == 3 and start_i == current_i and start_j == current_j:
        answer = max(answer, len(visited))
        return

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
    for start_i in range(N):
        for start_j in range(N):
            dfs(0, start_i, start_j, [])
    print(f'#{test_case} {answer}')