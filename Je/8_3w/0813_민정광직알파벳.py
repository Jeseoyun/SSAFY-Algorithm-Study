import sys
sys.stdin = open("Je/8_3w/input.txt")


'''
문제 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXAdrmW61ssDFAXq
'''

# 단어 세트에 알파벳 26개 모두 포함되어 있어야 함
# 최대한 많은 단어 세트를 만들어 주려고 함
# 최대한 많은??? -> 완탐..?
# 모든 경우의 수 구하기 -> 2^15개 조합... 흠 일단 해보쟈


def alphabet_counter(words):
    alphabet = set()

    for word in words:
        for chr in word:
            alphabet.add(chr)

    # 집합 원소의 개수가 26개이면 모든 알파벳이 있는 거시다
    if len(alphabet) == 26:  
        return True
    else:
        return False


def word_comb(idx, arr, comb, combs):
    if idx == len(arr):
        if alphabet_counter(comb):  # 모든 알파벳을 포함한 것만 저장
            combs.append(comb[:])
        return

    word_comb(idx+1, arr, comb, combs)
    word_comb(idx+1, arr, comb + [arr[idx]], combs)


def main():
    TC = int(input())

    for test_case in range(1, TC+1):
        N = int(input())
        words = [input().strip() for _ in range(N)]

        result = []
        word_comb(0, words, [], result)

        print(f"#{test_case} {len(result)}")


if __name__ == "__main__":
    main()