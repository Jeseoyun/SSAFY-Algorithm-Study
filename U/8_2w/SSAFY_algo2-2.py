'''
도착 좌표 주변 4방향이 0인 경우 멈출 수 없음 => -1
시작 지점에서 4방향 중 한 방향으로 벽을 만날 때까지 이동한다. 이동하면서 방문 체크
벽을 만나면 다른 방향 


'''
from collections import deque
from pprint import pprint
import sys
sys.stdin = open('algo2_sample_in.txt', 'r')
T = int(input())

# 좌표 이동용
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]



for test_case in range(1, T+1):
    M, N = map(int, input().split())    # board 행과 열
    board = [list(map(int, input().split())) for _ in range(M)]
    start_y, start_x , end_y, end_x = map(int, input().split())
    visited = [[0] * N for _ in range(M)]   # 방문 처리용 리스트
    move_cnt = 0    # 이동 거리

    result = search()

    print(f'#{test_case} {result}')