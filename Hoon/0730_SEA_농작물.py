#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    board = [list(map(int, input())) for _ in range(num)]

    middle_index = int(num/2)

    sum_val = 0

    for idx, val in enumerate(board):
        #2-0, 2-1, 2-2
        start_index = abs(middle_index - idx)
        cnt = num - start_index*2
        for i in range(cnt):
            sum_val += val[start_index + i]
            #print(val[start_index + i])

    print(f"#{test_case} {sum_val}")


