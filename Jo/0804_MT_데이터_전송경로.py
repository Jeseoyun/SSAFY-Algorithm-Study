from collections import deque
import sys

sys.stdin = open('algo2_sample_in.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    # 행, 열
    M, N = list(map(int, input().split()))
    # 네트워크
    network = [list(map(int, input().split())) for _ in range(M)]
    # 시작 위치와 목적지
    start_x, start_y, end_x, end_y = list(map(int, input().split()))
    # 최단거리 계산용
    dist_cnt = [[987654321] * N for _ in range(M)]
    # 시작점은 거리 0
    dist_cnt[start_x][start_y] = 0
    # 4방향. 상 우 하 좌
    dxy = [(-1,0), (0,1), (1,0), (0,-1)]
    
    # 큐에 삽입할 때 방향을 기억할 수 있도록 dxy 인덱스에 맞게 값을 추가함. 벽에 부딪혔을 때 방향을 기억하기 위해
    # queue = deque([(start_x, start_y, 0), (start_x, start_y, 1), (start_x, start_y, 2),(start_x, start_y, 3)])
    queue = deque([(start_x, start_y)])

    def bfs():
        while queue:
            point = queue.popleft()
            
            for x,y in dxy:
                nx = point[0] + x
                ny = point[1] + y

                #범위를 벗어났다면 continue
                if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                    continue

                #이전과 같은 방향으로 움직인 지점이 벽을 만난다면:
                if nx == end_x and ny == end_y and 0 <= (nx + x) <= M - 1 and 0 <= (ny + y) <= N -1 and network[nx + x][ny + y] == 1:
                    return dist_cnt[nx][ny]
                
                #거리 갱신
                if dist_cnt[point[0]][point[1]] + 1 < dist_cnt[nx][ny]:
                    dist_cnt[nx][ny] = dist_cnt[point[0]][point[1]] + 1
                    queue.append((nx, ny))

        return -1

    print(f'#{test_case} {bfs()}')

'''
젠장 또 -1 형이야

#1 -1
#2 -1
#3 -1
'''



