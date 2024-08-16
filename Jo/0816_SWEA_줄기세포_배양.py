# import sys
# sys.stdin = open('sample_input.txt', 'r')

dxy =[(0, 1), (1, 0), (-1, 0), (0, -1)]

T = int(input())

for test_case in range(1, T+1):
    # 세로, 가로, 배양시간
    N, M, K = map(int, input().split())

    input_cells = [list(map(int, input().split())) for _ in range(N)]

    # 넓은 범위로 배양할 것을 고려하여 board라는 큰 배열 만듦
    board = [[0]*(M+K*2) for _ in range(N+K*2)]

    cells = []
    for i in range(N):
        for j in range(M):
            X = input_cells[i][j]
            if X > 0:
                # 조정된 좌표 값을 넣어준다. 앞 X값은 활성 -> 비활성되는 시간. 뒤 X값은 비활성 -> 활성되는 시간
                board[i+K][j+K] = [X, X]
                cells.append([i+K, j+K])

    for time in range(K):
        # 세포가 새로 분열되면 저장
        new_cells = []
        for cell in cells:
            x, y = cell[0], cell[1]
            # 아직 세포 분열 전 -> 비활성 시간을 단축
            if board[x][y][1] > 0:
                board[x][y][1] -= 1
            # 활성이 되는 순간 세포 분열 -> new_cells 배열에 이동한 좌표값과 함께 시간값을 넣어줌
            elif board[x][y][1] == 0:
                X = board[x][y][0]
                for dx, dy in dxy:
                    if board[x+dx][y+dy] == 0:
                        new_cells.append([x+dx, y+dy, X])
                # 활성 시간 단축
                board[x][y][0] -= 1
            # 그 외에는 활성 시간이 있다면 단축
            else:
                if board[x][y][0] > 0:
                    board[x][y][0] -= 1

        # 새로운 태어난 세포는 cells 배열에 넣어주기
        for new_cell in new_cells:
            x, y, X = new_cell
            if board[x][y] == 0:
                board[x][y] = [X, X]
                cells.append([x, y])
            else:
                # 0이 아니고 동시에 이루어지려 한다면 생명력 수치가 더 높은 세포가 자리를 차지
                if board[x][y][0] < X:
                    board[x][y] = [X, X]

    answer = 0

    # 살아남은 세포 개수 세기
    for k in range(len(board)):
        for l in range(len(board[0])):
            # 번식한 흔적이 있고 활성화 상태라면 answer에 1을 더해준다
            if board[k][l] and board[k][l][0] > 0:
                answer += 1

    print(f'#{test_case} {answer}')