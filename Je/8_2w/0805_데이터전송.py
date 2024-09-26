# import sys
# sys.stdin = open("algo2_sample_in.txt")

from collections import deque


'''
경로를 탐색하는 문제 -> bfs를 사용하는 것이 유리함

진행 방향에 벽이 잇으면 방향을 바꾼다
기본적으로는 계속 전진해야 함...
그러면 큐에는 직진 방향이거나 벽에 부딪혔을 경우에만 값을 추가해야 함
'''


def network_path(network, N, M, start_point, end_point):
    dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = deque([start_point])

    visited = [[0]*M for _ in range(N)]
    # FLAG가 True이면 방향을 바꾸고 False이면 직진
    
    FLAG = True  # 출발지에서는 모든 방향으로 갈 수 있기 때문에 True로 초기값 설정

    while queue:
        print(queue, visited)
        x, y = queue.popleft()
        pre_vector = dxy

        for dx, dy in dxy:
            curr_vector = [dx, dy]
            nx, ny = x + dx, y + dy

            # 네트워크 범위를 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 진행 방향에 벽이 있는 경우
            if network[nx][ny] == 1:
                FLAG = True
                continue
            else:
                FLAG = False
                continue

            visited[nx][ny] = visited[x][y] + 1  # 방문 체크

            # 직진하는 경우(이전 백터와 현재 백터가 방향이 같음) 이거나(or)
            # FLAG가 True인 경우(진행 방향에 벽이 있었을 경우)
            # 큐에 값을 추가하여 다음 경로로 지정할 수 있다
            print(pre_vector, curr_vector)
            if (curr_vector in pre_vector) or FLAG:
                queue.append([nx, ny])

            pre_vector = [[dx, dy]]

            # 목적지에 도착한 경우
            if nx == end_point[0] and ny == end_point[1]:
                return visited[nx][ny]  # 출발지부터 도착지 경로의 거리를 반환

    return -1  # 목적지에 멈출 수 없는 경우


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    network = [list(map(int, input().split())) for _ in range(N)]
    points = list(map(int, input().split()))

    start_point = points[:2]  # 출발 지점
    end_point = points[2:]  # 도착 지점

    result = network_path(network, N, M, start_point, end_point)

    print(f"#{test_case} {result}")
