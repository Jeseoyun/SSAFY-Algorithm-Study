from collections import deque

#좌상2 우상2 우하2 좌하 시계방향 순서
dy = [-1,-2, -2,-1, 1,2, 2,1]
dx = [-2,-1, 1,2, 2,1, -1,-2]

def BFS(board, start_y, start_x, end_y, end_x, size):
    queue = deque([])

    if start_y == end_y and start_x == end_x:
        return 0

    cnt = 0

    queue.append((start_y, start_x, 0))

    while queue:
        y, x, cur_cnt = queue.popleft()

        #도착 검사
        if y == end_y and x == end_x:
            return cur_cnt

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= size or nx >= size:
                continue
            if board[ny][nx] == 1:
                continue
            
            board[ny][nx] = 1
            queue.append((ny, nx, cur_cnt + 1))

    return -1


def main():
    tc = int(input())

    for _ in range(tc):
        size = int(input())
        start_y, start_x = map(int, input().split())
        end_y, end_x = map(int, input().split())
        board = [[0] * size for _ in range(size)]
        board[end_y][end_x] = 2

        cnt = 0

        cnt = BFS(board, start_y, start_x, end_y, end_x, size)

        print(cnt)

    #최소 몇번만? BFS?
    #시작부터 같으면 바로 0 출력
    


if __name__ == "__main__":
    main()