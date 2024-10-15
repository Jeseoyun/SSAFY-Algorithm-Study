dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
inverse_dir = [2, 3, 0, 1]

is_cycle = 0

def DFS(board, visited, y, x, alphabet, size_y, size_x, dir):
    global is_cycle

    if is_cycle == 1:
        return

    for i in range(4):
        if dir != -1 and i == inverse_dir[dir]:
            continue
            
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
            continue

        if board[ny][nx] != alphabet:
            continue
        
        #사이클 검출
        if visited[ny][nx] == 1 and board[ny][nx] == alphabet:
            is_cycle = 1
            return

        if visited[ny][nx] == 1:
            continue
        
        visited[ny][nx] = 1
        DFS(board, visited, ny, nx, alphabet, size_y, size_x, i)



    return

def main():
    global is_cycle
    size_y, size_x = map(int, input().split())
    input_board = [input() for _ in range(size_y)]

    visited = [[0] * size_x for _ in range(size_y)]
    board = [[""] * size_x for _ in range(size_y)]

    for y in range(size_y):
        for x in range(size_x):
            board[y][x] = input_board[y][x]

    for y in range(size_y):
        for x in range(size_x):
            if visited[y][x] == 1:
                continue
            if is_cycle == 1:
                break
            DFS(board, visited, y, x, board[y][x], size_y, size_x, -1) 
        
        if is_cycle == 1:
            break

    if is_cycle == 0:
        print("No")
    elif is_cycle == 1:
        print("Yes")
    
    return

if __name__ == "__main__":
    main()