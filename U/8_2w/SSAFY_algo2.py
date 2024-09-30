'''
최단경로 찾기 => BFS로 풀자
데큐에 각 지점에 인접한 이동 가능한(1이 아닌) 좌표를 넣음
방문 표시도 하고
맨 앞에서 하나 꺼내서 해당 좌표로 이동
이동한 곳에서 데큐삽입->방문 표시->좌표이동 반복
인접한 이동 가능한 좌표가 없어 데큐에 더이상 삽입이 멈추고 데큐가 비면
도착한 것. => 도착 좌표와 현재 좌표를 비교하여 목적지 도착이 가능한지 확인

가지칠 수 있는 것
도착지점이 벽인 경우
바로 -1 반환

아니 근데 cnt 증가 어디서 해야하는 거지?
'''
from collections import deque
from pprint import pprint
import sys
sys.stdin = open('algo2_sample_in.txt', 'r')
T = int(input())

# 좌표 이동용
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def search():
    global move_cnt

    # 도착 지점 좌표의 좌표 값이 이미 1(벽)인 경우
    # 무조건 도달할 수 없기 때문에 return -1
    if board[end_y][end_x] == 1:
        return -1

    # 시작 지점 좌표 지정
    y, x = start_y, start_x

    # 데큐 생성 및 시작 지점 좌표 삽입
    deq = deque([(y,x)])
    # 방문 표시
    visited[y][x] = 1

    while deq:
        y, x = deq.popleft()
        
        for i in range(len(dy)):
            # 데큐 가장 앞에 있는 좌표(현재 위치) 기준으로 
            # 각 방향별로 새 좌표값 생성
            new_y, new_x = y + dy[i], x + dx[i]

            # 새 좌표가 board 크기를 넘어가면 
            # 이동 불가능 좌표이므로 다음 좌표로 이동
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M: continue

            # 새 좌표가 벽이라면
            if board[new_y][new_x] == 1: continue

            # 이미 방문한 곳이라면 다음 좌표로 이동
            if visited[new_y][new_x] == 1: continue

            # 위 경우가 모두 아니라면 해당 좌표로 이동 가능함
            # 데큐에 삽입 후 방문 처리
            deq.append([new_y, new_x])
            print(f'방문 좌표', new_x, new_y)
            # pprint(visited)
            visited[new_y][new_x] = 1
            move_cnt += 1
    
    if new_x == end_x and new_y == end_y:
        return move_cnt
    
    return -1



for test_case in range(1, T+1):
    M, N = map(int, input().split())    # board 행과 열
    board = [list(map(int, input().split())) for _ in range(M)]
    start_y, start_x , end_y, end_x = map(int, input().split())
    visited = [[0] * N for _ in range(M)]
    move_cnt = 0    # 이동 거리

    result = search()

    print(f'#{test_case} {result}')