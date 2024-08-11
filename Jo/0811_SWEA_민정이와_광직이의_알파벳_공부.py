import sys
sys.stdin = open("kwang_input.txt", "r")

T = int(input())

# 알파벳 26자
# alphabet_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u','v','w', 'x', 'y', 'z'}

for test_case in range(1, T + 1):
    # 단어 수
    N = int(input())
    word_list = [input() for _ in range(N)]
    # 조합 수
    comb_cnt = 0

    def dfs(words, idx):
        global comb_cnt
        if len(set(words)) == 26:
            comb_cnt += 1
            return
        if idx == N:
            return

        dfs(words + word_list[idx], idx + 1)
        dfs(words, idx + 1)

    dfs('', 0)

    print(f'#{test_case} {comb_cnt}')