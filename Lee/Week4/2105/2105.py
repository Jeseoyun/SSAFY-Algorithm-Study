import sys
import pprint
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dxy = [[-1, 1], [-1, -1], [1, 1], [1, -1]]

def solution(x, y, temp_list, visited, down_count, up_count):
    global result

    # 범위를 벗어 났을때
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    # 처음 값으로 돌아옴(다음값이 시작 값하고 같고 방문했던거면) and 현재 temp_list가 result보다 크면, 최소 4각형 이상, 내려간 만큼 올라가면 
    if visited[x][y] == 1 and [x,y] == start_idx and result < len(temp_list) and len(temp_list) >= 4 and up_count == down_count:
        result = max(result, len(temp_list))
        #print('결과 찾음', temp_list)
        #pprint.pprint(visited)
        return
    
    # 방문했던 위치면
    if visited[x][y]:
        return
    
    # 같은 종류의 디저트를 먹었으면
    if arr[x][y] in temp_list:
        return
    
    visited[x][y] = 1
    temp_list.append(arr[x][y])

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if [nx,ny] == [1,-1]:
            down_count += 1
        if [nx, ny] == [1,1]:
            up_count += 1
        solution(nx, ny, temp_list, visited, down_count, up_count)
    down_count = 0
    up_count = 0
    visited[x][y] = 0
    temp_list.pop()

for test_case in range(1, T+1):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    for i in range(N):
        for j in range(N):
            start_idx = [i,j]
            visited = [[0] * N for _ in range(N)]
            solution(i,j,[], visited, 0, 0)
    
    if result == 0:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {result}')