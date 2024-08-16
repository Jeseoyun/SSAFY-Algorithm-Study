import sys
sys.stdin = open("input.txt", "r")

max_length = -1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()

def DFS(board, y, x, can_cut_height, cur_height, length, size, visited):
    #탈출 조건 없음?
    global max_length
    max_length = max(max_length, length)


    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= size or nx >= size:
            continue
        if visited[ny][nx] == 1:
            continue
        
        #조건 만족시에만 DFS 진입
        if board[ny][nx] < cur_height:
            #디버깅
            visited[ny][nx] = 1
            print_board(visited)
            print()
            DFS(board, ny, nx, can_cut_height, board[ny][nx], length+1, size, visited)
            visited[ny][nx] = 0
            
        else:#작거나 같은 경우 중에서
            if can_cut_height < 0: # 이미 한번 자른 경우
                #return 지ㄹ
                continue
            elif board[ny][nx] - can_cut_height < cur_height:#잘라서 갈 수 있으면?
                #잘랐으니 더 못자름 == -1 대입
                #최선으로 자르는건 현재 높이에서 -1로 만드는게 최선
                #디버깅
                visited[ny][nx] = 1
                print_board(visited)
                print()
                DFS(board, ny, nx, -1, cur_height - 1, length+1, size, visited)
                visited[ny][nx] = 0

    return


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        num, height = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(num)]

        #print(board)
        global max_length
        max_length = -1
        max_height = -1
        for li in board:
            temp = max(li)
            max_height = max(max_height, temp)
        
        start_idx = []
        for y, li in enumerate(board):
            for x, elem in enumerate(li):
                if elem == max_height:
                    start_idx.append((y, x))
        
        #print(start_idx)

        for start_y, start_x in start_idx:
            visited = [[0]*num for _ in range(num)]
            
            print(start_y, start_x, "에서 출발하는 경우")
            #디버깅
            visited[start_y][start_x] = 1
            print_board(visited)
            print()

            DFS(board, start_y, start_x, height, board[start_y][start_x], 1, num, visited)
            visited[start_y][start_x] = 0

        print(f"#{test_case} {max_length}")


if __name__ == "__main__":
    main()