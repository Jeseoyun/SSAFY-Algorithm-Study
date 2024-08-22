import sys
import pprint
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def is_valid(x, y, dx, dy):
    # 전선을 놓을 수 있는지 확인
    while True:
        x += dx
        y += dy
        if x < 0 or x >= N or y < 0 or y >= N:  # 전원 연결 가능
            return True
        if arr[x][y] == 1:  # 코어나 전선이 이미 있는 경우
            return False

def set_wire(x, y, dx, dy, value):
    # 전선을 놓거나 제거
    length = 0
    while True:
        x += dx
        y += dy
        if x < 0 or x >= N or y < 0 or y >= N:
            break
        arr[x][y] = value
        length += 1
    return length

def dfs(idx, connected_cores, total_length):
    global max_cores, min_length

    if idx == len(core_list):
        if connected_cores > max_cores:
            max_cores = connected_cores
            min_length = total_length
        elif connected_cores == max_cores:
            min_length = min(min_length, total_length)
        return
    
    x, y = core_list[idx]
    for dx, dy in dxy:
        if is_valid(x, y, dx, dy):
            wire_length = set_wire(x, y, dx, dy, 1)
            dfs(idx + 1, connected_cores + 1, total_length + wire_length)
            set_wire(x, y, dx, dy, 0)  # 백트래킹
    dfs(idx + 1, connected_cores, total_length)  # 연결하지 않고 넘어감

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    core_list = []
    
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                core_list.append((i, j))
    
    max_cores = 0
    min_length = float('inf')
    
    dfs(0, 0, 0)
    
    print(f'#{test_case} {min_length}')
