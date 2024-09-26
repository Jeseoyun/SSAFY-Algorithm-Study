import sys
sys.stdin = open("input.txt", "r")

SIZE = 16

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
is_arrived = 0
def DFS(board, y, x):
    global visited
    global is_arrived

    # for li in board:
    #     print(li)
    # print()

    if board[y][x] == "3" or is_arrived:
        is_arrived = 1
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= SIZE or nx >= SIZE or board[ny][nx] == "1" or visited[ny][nx] == 1:
            continue
        visited[ny][nx] = 1
        DFS(board, ny, nx)
        visited[ny][nx] = 0

    return
    pass

T = 10
def main():
    global visited
    global is_arrived

    for test_case in range(1, T + 1):
        is_arrived = 0
        visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        tc = int(input())
        board = [list(input()) for _ in range(SIZE)]
        y=0
        x=0
        #print(board)

        for idx_y, li in enumerate(board):
            for idx_x, elem in enumerate(li):
                if elem == "2":
                    y = idx_y
                    x = idx_x
                    break

        visited[y][x] = 1
        DFS(board, y, x)
        print(f"#{test_case} {is_arrived}")
    pass

if __name__ == "__main__":
    main()