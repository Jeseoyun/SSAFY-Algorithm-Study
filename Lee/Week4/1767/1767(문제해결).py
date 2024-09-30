import sys
import pprint
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dxy = [[1,0], [-1,0], [0,1], [0,-1]]

def solution(idx, connected_cores, total_length):
    global max_cores, min_length
    
    # 모든 코어를 확인했으면
    if idx == len(core_list):
        if connected_cores > max_cores:
            max_cores = connected_cores
            min_length = total_length
        elif connected_cores == max_cores:
            # pprint.pprint(arr)
            min_length = min(min_length, total_length)
        return
    
    # 코어 있는 좌표값 저장
    x, y = core_list[idx]
    
    for dx, dy in dxy:
        # 초기 좌표 설정
        nx, ny = x, y
        
        wire_length = 0
        can_connect = True
        
        # 전선을 연결할 수 있는지 확인
        while 0 <= nx + dx < N and 0 <= ny + dy < N:
            nx += dx
            ny += dy
            
            if arr[nx][ny] == 1:
                can_connect = False
                break
            
            wire_length += 1
        
        # 전선을 연결할 수 있다면
        if can_connect and wire_length > 0:
            # 전선 설치
            nx, ny = x, y
            for _ in range(wire_length):
                nx += dx
                ny += dy
                arr[nx][ny] = 1

            # 다음 코어로 진행
            solution(idx + 1, connected_cores + 1, total_length + wire_length)
            
            # 전선 제거 (백트래킹)
            nx, ny = x, y
            for _ in range(wire_length):
                nx += dx
                ny += dy
                arr[nx][ny] = 0
                
    # 전선을 연결하지 않고 다음 코어로 진행
    solution(idx + 1, connected_cores, total_length)

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    core_list = []
    
    # 가장자리 제외한 코어 좌표 저장 리스트
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                core_list.append((i, j))
    
    max_cores = 0
    min_length = float('inf')
    
    solution(0, 0, 0)

    print(f'#{test_case} {min_length}')