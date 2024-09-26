T = int(input())


for tc in range(1, 1+T):
    BOARD_SIZE = int(input())
    board = [list(map(int, input())) for _ in range(BOARD_SIZE)]
    mid_num = BOARD_SIZE // 2
    result = []

    # 배열 길이만큼 돌기
    for y in range(BOARD_SIZE):
        result.append(board[y][abs(mid_num-y):BOARD_SIZE-abs(mid_num-y)])

    # 리스트 풀기
    result = sum(result, [])

    print(f'#{tc} {sum(result)}')