# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

'''
core_list : 코어 위치만 저장된 리스트 생성 ( 가장자리 core는 제외/이미 연결되어 있음)

core 수 만큼 for 문
- if 다음 값이 1이면 return
- 모든 코어 직선 연결 시도 후 max(result, line_sum)
    -> 직선 연결시마다 line_sum +=1
- 직선 연결: index가 N-1까지 dxy 한방향으로 계속 

'''

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
        # 다음 좌표 계산
        nx, ny = dx + x, dy + y
        
        wire_length = 0
        
        # 다음 좌표가 arr 범위 안이면
        while 0 <= nx < N and 0 <= ny < N:
            # 다음 좌표가 1이면 멈춤
            if arr[nx][ny] == 1:
                break
            
            # 직선 연결
            arr[nx][ny] = 1
            wire_length += 1
            nx, ny = nx + dx, ny + dy
        
        
        # 이동했으면
        if wire_length > 0:
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
            # print(x,y, dx, dy)
            # pprint.pprint(arr)
            
            # 전선 연결이 불가능하지만 전선을 추가해논 상태로 다음 idx에게 넘겨줌
            # 해결법: 전선 연결 가능을 사전 확인 or 연결하다 문제 발생시 1을 지우고 다음 idx로 넘어가야함.
            solution(idx + 1, connected_cores + 1, total_length + wire_length)
            
            nx, ny = x, y
            # 되돌아가면서 0처리
            for _ in range(wire_length):
                nx, ny = nx + dx, ny + dy
                arr[nx][ny] = 0
                
    # 이동 안했으면
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
    
    # pprint.pprint(arr)
    
    solution(0, 0, 0)
    print(min_length)
    # pprint.pprint(core_list)
    # pprint.pprint(arr)