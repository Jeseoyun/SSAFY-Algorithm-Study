# https://www.acmicpc.net/problem/9519 졸려
import sys

# 깜박 단어 만들기
# 짝수면 [0:2k+1] + 뒤에서 k번째 - 1 + [2k+1 : ]
# 홀수면 [0: ...

# 깜빡 전 단어 만들기

# set해서 1개만 있으면 원본 그대로 출력
# 일정 횟수 넘어가면 반복됨 -> 리스트에 저장하고 이미 있는 단어 만들어지면 멈춤

X = int(input())
word = list(input())

# 한 문자로만 구성된 단어면
if len(set(word)) == 1:
    print(''.join(word), end='')
    sys.exit(0)

# 앞, 뒤 단어 저장 리스트
front_word = []
back_word = []
# 결과값 계산 시 사용
result = word[:]
temp_word = ""
result_list = []

# arr 크기의 짝수는 오름차 순으로 붙이고 홀수는 내림차 순으로 뒤에 붙임
for i in range(len(word)):
    # 짝수와 맨끝 문자
    if i % 2 == 0 or i == len(word) - 1:
        front_word.append(i)
    # 그 외 홀수들 == 앞쪽에 끼인 값 들
    else:
        back_word.append(i)

back_word.sort(reverse=True)

for _ in range(X):
    for ch in front_word:
        temp_word += result[ch]

    for idx in back_word:
        temp_word += result[idx]

    result = list(temp_word)
    if result in result_list:
        break
    result_list.append(result)
    temp_word = ""

# print(result_list)
print(''.join(result_list[X % len(result_list) - 1]), end="")