#리팩토링 필요
import sys
sys.stdin = open("input.txt", "r")

#사각형 그리는 순서로 변경
# 좌하 우하 우상 좌상
dy = [1, 1, -1, -1]
dx = [-1, 1, 1, -1]

max_dist = float("-inf")

def print_board(visited, visited_num):
    for li in visited:
        for elem in li:
            print(elem, end=" ")
        print()
    print(visited_num)

def DFS(board, visited, y, x, end_y ,end_x, num, cur_dist, visited_num, cur_dir):
    global max_dist
    # if y == 0 and x == 2:
    #     print("도착!")

    if y == end_y and x == end_x:
        #최대값 판단
        if cur_dist == 2:
            return
        max_dist = max(max_dist, cur_dist)
        return
    
    #현재 방향으로 가던가, 다음 방향으로 가던가
    for i in range(cur_dir, cur_dir+2):
        if i == 4:
            continue

        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= num or nx >= num:
            continue
        #이미 지났거나, 혹은 도착점 값과 같으면
        if board[ny][nx] in visited_num or visited[ny][nx] == 1 :
            continue

        #그릴 사각형의 y좌표가 도착보다 작아지는 경우
        if ny < end_y:
            continue

        visited[ny][nx] = 1
        #디버깅
        visited_num.add(board[ny][nx])

        #print_board(visited, visited_num)
        DFS(board, visited, ny, nx, end_y, end_x, num, cur_dist+1, visited_num, i)
        visited[ny][nx] = 0
        visited_num.remove(board[ny][nx])
    

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        global max_dist
        max_dist = float("-inf")

        num = int(input())
        board = [list(map(int, input().split())) for _ in range(num)]
        

        for end_y in range(num):
            for end_x in range(num):
                visited = [[0] * num for _ in range(num)]
                visited_num = set()
                visited[end_y][end_x] = 2

                #자기 자리로 되돌아왔을 경우를 처리해주기 위해 자리를 기준으로 4방향에서 시작
                #사각형을 아래로만 그리도록 가지치기
                for i in range(0,1):
                    start_y = end_y + dy[i]
                    start_x = end_x + dx[i]
                    if start_y < 0 or start_x < 0 or start_y >= num or start_x >= num:
                        continue
                    #현재랑 다음이랑 같으면
                    if board[start_y][start_x] == board[end_y][end_x]:
                        continue

                    visited[start_y][start_x] = 1
                    visited_num.add(board[start_y][start_x])
                    #디버깅
                    #print_board(visited, visited_num)
                    DFS(board, visited, start_y, start_x, end_y ,end_x, num, 1, visited_num, 0)
                    visited[start_y][start_x] = 0
                    visited_num.remove(board[start_y][start_x])

        answer = 0
        if max_dist == float('-inf'):
            answer = -1
        else:
            answer = max_dist

        print(f"#{test_case} {answer}")

if __name__ == "__main__":
    main()