from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

def main():
    size_y, size_x = map(int, input().split())
    st = "KAKTUS"
    input_board = [input() for _ in range(size_y)]


    board = [[0] * size_x for _ in range(size_y)]
    for y, li in enumerate(input_board):
        for x, elem in enumerate(li):
            board[y][x] = elem

    visited = [[0] * size_x for _ in range(size_y)]
    cnt = 0
    
    queue = deque([])
    # new_queue = deqeue([])

    # 물 먼저 넣고, 비버 넣고
    waters = []
    S = []
    D = []

    for y in range(size_y):
        for x in range(size_x):
            if board[y][x] == "*":
                #원본 변형해서 방문처리
                waters.append((y, x, "*" ,0))
            elif board[y][x] == "S":
                #visited를 사용해서 방문처리
                S.append((y, x, "S" ,0))
                visited[y][x] = 1

            elif board[y][x] == "D":
                D.append((y, x))
    
    for elem in waters:
        queue.append(elem)
    
    queue.append(S[0])

    while queue:
        y, x, board_type, time = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                continue

            if board_type == "*":
                if board[ny][nx] == "X" or board[ny][nx] == "D" or board[ny][nx] == "*":
                    continue
                
                board[ny][nx] = "*"
                queue.append((ny, nx, "*", time+1))
            
            elif board_type == "S":
                if board[ny][nx] == "D":
                    cnt = time + 1
                    break
                if board[ny][nx] == "X" or board[ny][nx] == "*":
                    continue
                if visited[ny][nx] == 1:
                    continue

                queue.append((ny, nx, "S", time+1))
                visited[ny][nx] = 1
        
        if cnt != 0:
            break

    if cnt == 0:
        print(st)
    else: print(cnt)

if __name__ == "__main__":
    main()