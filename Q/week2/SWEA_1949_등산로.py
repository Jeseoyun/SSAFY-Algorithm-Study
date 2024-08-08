'''
DFS에서 재귀를 활용하라는 것은 이유가 있는 것 같습니다...
스택을 이용한 풀이 시도를 진행하다가 꺽였습니다
main() 함수를 사용하고 싶었는데 그렇게 될 경우 이미 많은 매개변수에 더 많은 값을 던져줘야 해서 main()을 빼고 진행해 보았습니다
'''

# 방향 벡터: 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, height, cut, length, visited): # 현재의 x, y의 좌표, 현재 지점의 height, cut 사용 여부, 등산로 길이, visited 배열을 매개변수로 받습니다
    global answer
    answer = max(answer, length)    # DFS를 수행할 때 마다 최대값을 갱신하는 방식으로 등산로 최대 길이를 구했습니다

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if arr[nx][ny] < height:  # 다음 지점이 현재 지점보다 낮은 경우
            visited[nx][ny] = True
            dfs(nx, ny, arr[nx][ny], cut, length + 1, visited)
            visited[nx][ny] = False 
        elif cut and arr[nx][ny] - k < height:  # 깎아서 갈 수 있는 경우
            visited[nx][ny] = True
            dfs(nx, ny, height - 1, False, length + 1, visited) 
            # arr의 값을 바꾸게 되면 다시 바꾸기 위해 생성되는 변수들이 너무 많기에 그냥 arr[i][j] 대신 height를 사용했습니다
            visited[nx][ny] = False

# 메인 시작
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_value = 0
    max_pos = []
    answer = 0

    # 가장 높은 위치 찾기
    # max 값을 찾고 max값과 같은 value를 가지고 있는 곳의 pos를 튜플의 형태로 넣어줍니다 
    for i in range(n):
        for j in range(n):
            if max_value < arr[i][j]:
                max_value = arr[i][j]
                max_pos = [(i, j)]
            elif max_value == arr[i][j]:
                max_pos.append((i, j))
                

    # 각 봉우리에서 DFS 탐색 시작
    for pos in max_pos:
        visited = [[False] * n for _ in range(n)]
        x, y = pos  # 튜플을 언패킹한 후 해당 위치부터 DFS 시작
        visited[x][y] = True
        dfs(x, y, arr[x][y], True, 1, visited)

    print(f'#{test_case} {answer}')