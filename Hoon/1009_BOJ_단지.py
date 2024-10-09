from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(board, visited, start_y, start_x, size):
    cnt = 1
    queue = deque([])
    queue.append((start_y, start_x))
    visited[start_y][start_x] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= size or nx >= size:
                continue
            
            if visited[ny][nx] == 1:
                continue

            if board[ny][nx] == 0:
                continue

            cnt += 1
            queue.append((ny, nx)) 
            visited[ny][nx] = 1  

    return cnt

def main():
    size = int(input())

    board = [[0] * size for _ in range(size)]
    visited = [[0] * size for _ in range(size)]

    input_board = [input() for _ in range(size)]

    for y in range(size):
        for x in range(size):
            board[y][x] = int(input_board[y][x])
    
    list_house = []

    for y in range(size):
        for x in range(size):
            if board[y][x] == 1 and visited[y][x] == 0:
                list_house.append(BFS(board, visited, y, x, size))

    print(len(list_house))
    list_house.sort()

    for elem in list_house:
        print(elem)


if __name__ == "__main__":
    main()