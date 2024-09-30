import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(idx, selected_set):
    global max_count
    
    # 주어진 단어를 모두 탐색한 경우 종료
    if idx == len(words):
        # 26개의 알파벳을 모두 포함한 경우
        if len(selected_set) == 26:
            max_count += 1
        return
    
    # 현재 단어를 포함하는 경우
    new_set = selected_set.union(words[idx])
    dfs(idx + 1, new_set)
    
    # 현재 단어를 포함하지 않는 경우
    dfs(idx + 1, selected_set)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    words = [input().strip() for _ in range(N)]  
    words = [set(word) for word in words]

    max_count = 0

    dfs(0, set())  # 초기 호출 시 빈 set과 함께 시작
    
    print(f'#{test_case} {max_count}')