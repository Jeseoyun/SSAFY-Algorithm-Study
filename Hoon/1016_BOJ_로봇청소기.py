from collections import deque

# 0 북, 1 동, 2 남, 3 서
inverse_dir = [2, 3, 0, 1]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def main():
    size_y, size_x = map(int, input().split())
    start_y, start_x, strart_dir = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(size_y)]
    visited = [[0] * size_x for _ in range(size_y)]

    cnt = 0
    q = deque([])

    if board[start_y][start_x] != 1:
        q.append((start_y, start_x, strart_dir))
        visited[start_y][start_x] = 1
        cnt += 1

    while q:
        y, x, cur_dir = q.popleft()

        if visited[y][x] == 0:
            visited[y][x] = 1
            cnt += 1
        
        is_dirt = False

        #검사
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                continue
            if visited[ny][nx] == 0 and board[ny][nx] == 0:
                is_dirt = True

        #청소할 곳이 없으면
        if is_dirt == False:
            ny = y + dy[inverse_dir[cur_dir]]
            nx = x + dx[inverse_dir[cur_dir]]
            
            if board[ny][nx] == 1:
                break
            else:
                q.append((ny, nx, cur_dir))
                continue

        #청소할 곳이 있으면
        if is_dirt == True:
            ny = -1
            nx = -1
            next_dir = -1
            for i in range(4):
                next_dir = (cur_dir + 4 - i - 1) % 4
                ny = y + dy[next_dir]
                nx = x + dx[next_dir]
                if ny < 0 or nx < 0 or ny >= size_y or nx >= size_x:
                    continue
                if visited[ny][nx] == 0 and board[ny][nx] == 0:
                    #다음 위치 찾음
                    break
            q.append((ny, nx, next_dir))

    print(cnt)

    return


if __name__ == "__main__":
    main()