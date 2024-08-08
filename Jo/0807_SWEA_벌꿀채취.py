from itertools import combinations

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    N, M, C = list(map(int, input().split()))
    # 벌통
    honey_bin = [list(map(int, input().split())) for _ in range(N)]
    # 총 수익 계산
    answer = 0

    # 각 벌통의 제곱합을 구할 함수
    def honey_square_sum(part):
        # 최대 양보다 크면 음수를 줘버림 (어차피 벌통들이 다 양수니까)
        if sum(part) > C:
            return -1
        square_sum = sum([num ** 2 for num in part])
        return square_sum

    # 최댓값 구하기
    def honey_max(part):
        max_value = 0
        lst = []
        # 1개부터 M개까지 뽑는 조합의 제곱합을 구하고 그 중에 최댓값을 도출함
        for n in range(1, M + 1):
            combs = list(combinations(part, n))
            for comb in combs:
                lst.append(honey_square_sum(comb))
            max_value = max(max(lst),max_value)
        return max_value
    
    # 벌통 두 개를 선택하는 경우를 4중 for문으로 도출
    for i1 in range(N):
        for j1 in range(N-M+1):
            first_part = honey_bin[i1][j1: j1 + M]
            first_part_max = honey_max(first_part)
            for i2 in range(i1, N):
                for j2 in range(N-M+1):
                    # 같은 행이고 첫 번째 부분 겹쳐버리면 빠꾸시킴
                    if i1 == i2 and j2 < j1 + M:
                        continue
                    second_part = honey_bin[i2][j2: j2 + M]
                    second_part_max = honey_max(second_part)
                    answer = max(first_part_max + second_part_max, answer)

    print(f'#{test_case} {answer}')



