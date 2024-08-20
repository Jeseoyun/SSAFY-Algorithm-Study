'''
입력받은 문자열을 조합을 구현하여 단어를 이어 붙이고 그 이어 붙인 단어를 check 함수로 보내줌
받은 check 함수에서 list(set(string)를 이용해서 중복되는 알파벳들을 싹 다 날려줌
그 후 알파벳 26개가 다 있는지 체크하고 없을 경우 False 중복체크 다 했는데 남은 갯수가 26개면 true 반환
'''


def check(string):
    string = list(set(string))
    if len(string) != 26:
        return False
    elif len(string) == 26:
        return True


def dfs(idx, depth, string):
    global answer

    if check(string):
        answer += 1
    if depth == n:
        return

    for i in range(idx, n):
        dfs(i + 1, depth + 1, string + words[i])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    words = [input().strip() for _ in range(n)]
    vis = [False * n]
    answer = 0
    dfs(0, 0, "")
    print(f'#{test_case} {answer}')