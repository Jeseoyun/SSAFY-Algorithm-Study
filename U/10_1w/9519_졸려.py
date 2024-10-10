'''
https://www.acmicpc.net/problem/9519

ㅡㅡ 시간초과남
나보고 어쩌라고

글자에 주기가 있음
주기는 짝수일 때와 홀수일 때 다른 것 같음
2, 3은 예외
짝수는 len(txt) -1 의주기마다 반복함
홀수는 len(txt) -2의 주기마다 반복
'''

N = int(input())
txt = input()

def recover_txt(word):
    result = ''

    # 짝수일 때
    if len(txt) % 2 ==0:
        # 갈라진 문자들 붙이기
        for i in range(0, len(word)-1, 2):
            result += word[i]
        # 끼워진 문자들 복구
        for i in range(-1, -len(word), -2):
            result += word[i]

    else:
        # 갈라진 문자들 붙이기
        for i in range(0, len(word), 2):
            result += word[i]
        # 끼워진 문자들 복구
        for i in range(-2, -len(word), -2):
            result += word[i]

    return result

for cnt in range(N):
    txt = recover_txt(txt)

print(txt)
