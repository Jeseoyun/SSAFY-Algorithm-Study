from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
sys.stdin = open("input.txt", "r")

NUM = 3
#왼쪽 위 오른쪽 순
dy = [0, -1, 0]
dx = [-1, 0, 1]

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()


def main():
    size_y, size_x, dist = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size_y)]

    # 궁수 위치를 맨 아래줄 좌표를 기준으로 조합으로 dfs (이터툴즈도 되고)
    # 궁수 위치를 정했으면 지우는 시뮬레이션.
    # 적 탐색을 좌하단에서부터 시작?
    # 위치랑 일정 거리 내면 지우기
    # 아래로 한칸 전진

    li = [x for x in range(size_x)]
    # print(li)

    positions = list(combinations(li, 3))
    positions.sort()

    # print(positions)
    max_point = 0
    
    # for x_list in [(0, 2, 3)]:
    for x_list in positions:
        cur_point = 0
        start_y = size_y - 1
        c_board = deepcopy(board)

        #한 라인당 BFS 탐색
        visited = [[0] * size_x for _ in range(size_y)]
        for _ in range(size_y):
            # 궁수가 죽이기, 제거한 숫자 count
            # 쐈는지 확인
            is_shooted = [0] * 3
            #방문처리
            # BFS 시작점을 동시에 3곳
            queue = deque([])

            for idx, x in enumerate(x_list):
                #거리 1에서 이미 죽인 적이 있으면 아예 안 들어감
                if visited[start_y][x] == 0 and c_board[start_y][x] == 1:
                    cur_point += 1
                    c_board[start_y][x] = 0
                    visited[start_y][x] = 1
                    # print(queue)
                    # print(cur_point)
                    # print_board(visited)
                    continue
                
                #현재 x좌표, 현재 y좌표, 몇번궁수, 현재거리
                queue.append((start_y, x, idx, 1))
                visited[start_y][x] = 1
                # print(queue)
                # print(cur_point)
                # print_board(visited)

            while queue:
                y, x, who, cur_dist = queue.popleft()
                
                if is_shooted[who] == 1:
                    continue
                if cur_dist >= dist:
                    continue
                
                for i in range(3):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if is_shooted[who] == 1:
                        continue

                    if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                        continue
                    if visited[ny][nx] == 1 and c_board[ny][nx] == 1:
                        is_shooted[who] = 1
                        continue
                    
                    #쏜애를 visited 하지 않는 이유는 또 쏠수 있기 때문?
                    #그치만 쏜 애는 count를 안해줘야하는데?
                    if c_board[ny][nx] == 1:
                        if visited[ny][nx] == 0:
                            cur_point += 1
                            c_board[start_y][x] = 0
                        is_shooted[who] = 1
                        visited[ny][nx] = 1
                        # print(queue)
                        # print(cur_point)
                        # print_board(visited)
                        continue
                    
                    queue.append((ny, nx, who, cur_dist + 1))
                    visited[ny][nx] = 1

                    # print(queue)
                    # print(cur_point)
                    # print_board(visited)

            # 맨 뒷줄 제거, 맨 앞줄 추가 == 한줄 전진
            start_y = start_y - 1

        max_point = max(max_point, cur_point)
    
    print(max_point)

    return

if __name__ == "__main__":
    main()