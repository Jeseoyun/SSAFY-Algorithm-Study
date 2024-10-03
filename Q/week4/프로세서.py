'''
문제조건
1. 최대한 많은 core에 전원을 연결하라
2. 전선의 길이는 최소가 되게끔

우선순위는 1번이 우선 순위
'''

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(depth, total_length, core_count):
    global min_length, answer_max_core_count

    if answer_max_core_count < core_count:              # 우선 순위 1번 체크 먼저
        min_length = total_length                       # 현재 dfs에 들어온 코어의 수가 체크된 코어 수보다 많을 경우
        answer_max_core_count = core_count              # 우선 순위에 따라 바로 길이 수정, 코어 갯수 수정
    elif answer_max_core_count == core_count:           # 만약 코어 수가 같을 경우 우선 순위 2번에 따라
        min_length = min(total_length, min_length)      # 최소 길이 확인 후 짧은 길이로 교체

    if depth == count:                                  # 만약 depth가 코어의 수만큼 돌았을 경우 return
        return

    for d in range(4):                                  # 4방향 다 확인 진행
        cur_x, cur_y = core_list[depth]                 
        nx, ny = cur_x, cur_y
        core_line = 0                                   # core가 전원 연결되기 위한 전선길이 체크
        flag = False

        while 0 < nx < n - 1 and 0 < ny < n - 1:        # 끝에 닿을 때까지 계속 진행
            nx = nx + dx[d]
            ny = ny + dy[d]
            if arr[nx][ny] != 0:                        # 이동 경로에 코어나 전선이 있을 경우
                flag = True                             # 그 경로는 못 쓰는 경로
                break
            core_line += 1                              # 한번 while 돌 때 마다 길이 1씩 더하기

        if flag:                                        # 못 쓰는 경로는 아래 과정 필요없으니 패스
            continue

        nx, ny = cur_x, cur_y                           # 지나가는 경로를 모두 전선으로 바꿔주기 위해 nx와 ny를 다시 현재 x,y로 바꿈                  
        for i in range(core_line):                      # 전선 길이만큼 for문 진행
            nx = nx + dx[d]                             
            ny = ny + dy[d]     
            arr[nx][ny] = 2                             # 경로를 싹 다 2로 바꿔 충돌 체크할 수 있도록 함

        dfs(depth + 1, total_length + core_line, core_count + 1)    # 다음 코어 연결하러

        while cur_x != nx or cur_y != ny:               # 완전 탐색의 로직은 체크를 진행하기 위한 변수들을 바꿔주고
            arr[nx][ny] = 0                             # 완전 탐색 함수로 보내고
            nx = nx - dx[d]                             # 재귀가 끝나고 나오면 바꿔준 변수들을 복구시키는 것이 기본 로직
            ny = ny - dy[d]                             # arr를 코어가 연결되기 전으로 바꿔줌

    dfs(depth + 1, total_length, core_count)            
    # 아무리 해도 연결 안되는 코어가 있을 수 있으니 & 
    # 연결하지 않고 다른 코어 연결하는 경우가 더 많이 연결할 수 있고 전선이 더 짧을 경우가 있을 수 있다
    # 코어 연결 안하고 다음 코어 체크하러

# 입력받는 부분
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    core_list = []
    min_length = 1234567
    answer_max_core_count = 0

    # 끝에 있는 애들은 이미 연결되어 있으니 연결안되어 있는 애들로만
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j] == 1:
                count += 1
                core_list.append((i, j))

    dfs(0, 0, 0)

    print(f'#{test_case} {min_length}')
