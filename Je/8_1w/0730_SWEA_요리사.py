'''
문제링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH
'''

import itertools


def half_split(arr, comb, idx, result):
    if len(comb) == len(arr) // 2:
        tmp = (comb[:], [i for i in arr if i not in comb])
        result.append(tmp)

    for i in range(idx, len(arr)):
        comb.append(arr[i])
        half_split(arr, comb, i + 1, result)
        comb.pop()


def calculate_synergy(food, synergy):
    food_synergy = 0
    # 선택한 요리에서 2가지 재료를 조합할 수 있는 경우의 수 찾기
    food_pairs = itertools.combinations(food, 2)
    for i, j in food_pairs:
        food_synergy += synergy[i][j] + synergy[j][i]

    return food_synergy  # 시너지 계산 결과값을 반환


def min_taste_diff(synergy, N):
    # 음식 A 재료 / 음식 B 재료 나누기
    # -> N개의 재료를 N//2개로 나눈다
    food_half_split = []
    half_split(range(N), [], 0, food_half_split)

    min_diff = float('inf')

    for a_ing, b_ing in food_half_split:
        food_a = calculate_synergy(a_ing, synergy)
        food_b = calculate_synergy(b_ing, synergy)

        min_diff = min(min_diff, abs(food_a - food_b))

    return min_diff


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        synergy = [list(map(int, input().split())) for _ in range(N)]

        result = min_taste_diff(synergy, N)

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()