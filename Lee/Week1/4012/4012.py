import sys
import itertools
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 식재료 배열
    food_arr = range(0, N)

    # A 와 B가 반반 나눠 가질 개수
    half = N // 2

    # A가 half개씩 고를수 있는
    A_food = list(itertools.combinations(food_arr, half))
    B_food = []
    result = float('inf')

    # A_food 리스트에서 경우의 수를 하나씩 돌아가면서 진행
    for a_food in A_food:
        # 전체 food_arr를 전부 둘러봄
        for num in food_arr:
            # 만약 이번에 A가 가져간 음식들중에 없는 음식이면 B_food에 추가 == A가 고르고 남은 음식
            if num not in a_food:
                B_food.append(num)

        # 반 가져간 음식중에서 A가 2개씩 조합할 경우들의 시너지 합 구함
        a_synergy = 0
        a_two_pick = itertools.combinations(a_food, 2)
        for i, j in a_two_pick:
            a_synergy += arr[i][j] + arr[j][i]

        # 반 가져간 음식중에서 B가 2개씩 조합할 경우들의 시너지 합 구함
        b_synergy = 0
        b_two_pick = itertools.combinations(B_food, 2)
        for i, j in b_two_pick:
            b_synergy += arr[i][j] + arr[j][i]
        
        # A시너지 - B시너지의 절댓값 계산 후 result와 비교하여 최소값 갱신
        if abs(a_synergy - b_synergy) < result:
            result = abs(a_synergy - b_synergy)

        # A가 i일때 마다 B가 남은 음식 담아야하므로 초기화
        B_food = []

    print(f'#{test_case} {result}')
