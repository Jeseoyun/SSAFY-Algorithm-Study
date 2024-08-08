from collections import deque
import sys
sys.stdin = open("input.txt", "r")

# 0. 잘못 풀었던 BFS + 모든 지점 방문처리 => 같은 지점을 다시 지나야만 도착하는 케이스 처리 불가
# Why? 기존 문제들은 해당 장소에 도착시 어디든 갈 수 있었음. 이번 문제는 그럴 수 없음.

# 1. 반장님의 부딪히는 곳에서만 방문 처리하는 BFS
# 다만 지나온 길을 큐에 넣지 않도록 방문처리한 지점을 도달시 아무것도 넣치 않고 잘 반환해줘야함.

visited = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(board, start_y, start_x, end_y, end_x, size_y, size_x):
    queue = deque([])
    queue.append((start_y, start_x, 0, 0))#좌표, 좌표, 거리, 이전에 움직인 방향
    queue.append((start_y, start_x, 0, 1))
    queue.append((start_y, start_x, 0, 2))
    queue.append((start_y, start_x, 0, 3))
    is_arrived = 0
    dist = 0

    while queue:
        y, x, cur_dist, cur_dir = queue.popleft()
        
        # 탈출 코드 위치가 틀렸다.
        # #목표 도착시 탈출
        # if y == end_y and x == end_x:
        #     is_arrived = 1
        #     dist = cur_dist
        #     break 

        #이전 방향으로 계속 가는지 판단
        ny = y + dy[cur_dir]
        nx = x + dx[cur_dir]

        #다음 좌표가 벽인 경우 == 부딪힘
        #방문 처리를 벽에 만나는 경우에만 해준다.
        if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x or board[ny][nx] == 1:
            #목표 도착시 탈출
            if y == end_y and x == end_x:
                is_arrived = 1
                dist = cur_dist
                break 
            
            if visited[y][x] == 1:#이전에 멈췄던 곳이면.
                continue
            else:
                visited[y][x] = 1

            for i in range(4):
                new_y = y + dy[i]
                new_x = x + dx[i]
                #큐에 추가하면 안되는 경우 처리
                if new_y < 0 or new_x < 0 or new_y >= size_y or new_x >= size_x or board[new_y][new_x] == 1:
                    continue
                queue.append((new_y, new_x, cur_dist+1, i))

        else:#안 부딛히는 경우
            queue.append((ny, nx, cur_dist+1, cur_dir))

    if is_arrived == 0:
        return -1
    else:
        return dist


def main():
    test_case = int(input())
    global visited

    for tc in range(1, test_case+1):
        size_y, size_x = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(size_y)]

        start_y, start_x, end_y, end_x = map(int, input().split())

        visited = [[0]*size_x for _ in range(size_y)]

        #print(board)
        #print(start_y, start_x, end_y, end_x)

        dist = BFS(board, start_y, start_x, end_y, end_x, size_y, size_x)


        print(f"{tc} {dist}")

if __name__ == "__main__":
    main()