#뭐 틀렸지?
#테케만 맞아서 모르겠음

import sys
sys.stdin = open("input.txt", "r")

MAX_ALPHABET_CNT = 26

word_set_num = 0

def DFS(words, num, alphabet_set, idx, alphabet_cnt, is_selected):
    global word_set_num

    if alphabet_cnt == MAX_ALPHABET_CNT and is_selected == True:
        #이미 만들어졌어도 추가해서 단어 세트로 만들어버릴 수 있으니,
        #return하지 않는다.
        word_set_num += 1
        #print(alphabet_set)

    if idx >= num:
        return
    
    #저번에 배운 참조 함정
    #print(id(alphabet_set))

    #단어 추가 안 한 경우
    DFS(words, num, alphabet_set, idx+1, alphabet_cnt, False)

    #단어 추가 한 경우
    temp_alphabet_set = []

    for letter in words[idx]:
        if letter in alphabet_set:
            continue
        alphabet_set.add(letter)
        temp_alphabet_set.append(letter)
        alphabet_cnt += 1

    DFS(words, num, alphabet_set, idx+1, alphabet_cnt, True)
    #초기화
    for letter in temp_alphabet_set:
        alphabet_set.remove(letter)
        alphabet_cnt -= 1


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        global word_set_num
        word_set_num = 0

        alphabet_set = set()
        alphabet_cnt = 0

        num = int(input())
        words = [input().lower() for _ in range(num)]

        # print(words)

        DFS(words, num, alphabet_set, 0, alphabet_cnt, False)

        print(f"#{test_case} {word_set_num}")

if __name__ == "__main__":
    main()