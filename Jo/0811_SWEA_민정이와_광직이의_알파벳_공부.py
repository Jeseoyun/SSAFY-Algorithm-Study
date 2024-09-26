from itertools import combinations

# import sys
# sys.stdin = open("kwang_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    #단어 수
    N = int(input())
    #단어들
    words = [input().strip() for _ in range(N)]

    answer = 0

    #각 조합을 문자열로 바꾸고 문자열을 집합으로 변환하여 길이를 연산. 26일 경우 1 추가
    for i in range(1, N + 1):
        word_combs = list(combinations(words, i))
        for word_comb in word_combs:
            words_to_str = "".join(word_comb)
            letters_set = set(words_to_str)
            if len(letters_set) == 26:
                answer += 1

    print(f'#{test_case} {answer}')