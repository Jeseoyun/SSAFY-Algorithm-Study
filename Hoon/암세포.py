from collections import deque
import sys
sys.stdin = open("input.txt", "r")

#BFS
#visited에서 다익스트라
#이미 차지하고 있으면 가지 않고, "동시에" 하려고 하면 차지
cnt = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = []

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()


def BFS(board, end_time, size_y, size_x):
    global cnt

    q = deque([])

    for y in range(size_y):
        for x in range(size_x):
            if board[y][x] != 0:
                #y좌표, x좌표, 현재시간, 해당 좌표에서 머무른 시간, 생명력
                q.append((y, x, 0, 0, board[y][x]))
                #append할 때마다 cnt+1
                cnt += 1
                #visited.add((y, x, 0))
                #생명력, 추가된 시간
                visited[y+300][x+300] = [board[y][x], 0]

    while q:
        y, x, cur_time, waiting_time, hp = q.popleft()
        if cur_time > end_time:
            continue
        #out of range 검사 없음!

        #이미 내가 생명력이 더 쌘 줄기세포한테 먹혔으면?
        if hp < visited[y+300][x+300][0]:
            continue

        #아직 시간이 남았으면
        if waiting_time < hp:
            q.append((y, x, cur_time+1, waiting_time+1, hp))
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            #visited에서 시간대 비교 해줘야함
            if visited[300+ny][300+nx][0] != 0:
                #언제 저장됐던거지? 시간이 같으면
                if visited[300+ny][300+nx][1] == cur_time:
                    #더 큰 생명력으로 대체
                    visited[300+ny][300+nx][0] = max(hp, visited[300+ny][300+nx][0])
                    q.append((ny, nx, cur_time+1, 0, visited[300+ny][300+nx][0]))
                    # print(f"{ny}, {nx}")
                else:
                    continue
            else:
                visited[300+ny][300+nx][0] = hp
                visited[300+ny][300+nx][0] = cur_time
                q.append((ny, nx, cur_time+1, 0, hp))
                # print(f"{ny}, {nx}")
                cnt += 1


T = int(input())
def main():
    global cnt
    global visited
    for test_case in range(1, T + 1):
        cnt = 0
        size_y, size_x, end_time = map(int, input().split())

        board = [list(map(int, input().split())) for _ in range(size_y)]

        #방문처리를 set으로?
        visited = [[[0 for _ in range(2)] for _ in range(700)] for _ in range(700)]
        # print(id(visited[0][0]))
        # print(id(visited[0][1]))
        # print(id(visited[1][0]))

        # print_board(board)
        # print()
        # print_board(visited)

        BFS(board, end_time, size_y, size_x)

        print(f"#{test_case} {cnt}")

if __name__ == "__main__":
    main()