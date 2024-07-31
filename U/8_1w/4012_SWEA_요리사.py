import sys
sys.stdin = open('4012_input.txt', 'r')

T = int(input())


for tc in range(1, T+1):
    # 식재료 수 N
    N = int(input())

    food_score = [list(map(int, input().split())) for _ in range(N)]
    print(food_score)

    for i in range(N):
        