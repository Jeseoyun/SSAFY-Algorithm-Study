# 이동할 방향: 왼쪽 아래, 오른쪽 아래, 오른쪽 위, 왼쪽 위
dxy = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

def dfs(i, j, direction, count):
    global answer, start_i, start_j, dessert_list

    # 방향이 4번을 넘는 경우 종료
    if direction == 4:
        return

    ni, nj = i + dxy[direction][0], j + dxy[direction][1]

    # 출발점으로 돌아왔을 때 움직임이 4번 이상 있어야 사각형이 완성되므로 count가 4이상인 경우
    if ni == start_i and nj == start_j and count >= 4:
        answer = max(answer, count)
        return

    # 다음 위치가 범위 내에 있고, 아직 방문하지 않은 디저트 종류일 때
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in dessert_list:
        dessert_list.append(arr[ni][nj])  # 디저트 종류를 리스트에 추가
        dfs(ni, nj, direction, count + 1)  # 현재 방향으로 계속 이동
        dfs(ni, nj, direction + 1, count + 1)  # 다음 방향으로 전환하여 이동
        dessert_list.pop() 

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    # 모양이 마름모 모양으로 되기에 다음과 같은 방식으로 x와 y설정 가능
    for i in range(N-2):
        for j in range(1, N-1):
            start_i, start_j = i, j     # 시작 지점 설정
            dessert_list = [arr[i][j]]  # 현재 위치의 디저트를 리스트에 추가
            dfs(i, j, 0, 1)             # DFS 시작, 초기 방향은 0, 카운트는 1

    print(f'#{test_case} {answer}')
