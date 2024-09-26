T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input()))for _ in range(N)]

    # 가운데 줄의 인덱스를 가져오기 위한 과정입니다. N은 홀수라는 조건이 있으므로 다음과 같이 진행하였습니다.
    start_point = int(N/2)
    answer = 0

    for i in range(start_point+1):              # 0부터 절반의 위치까지 진행하기 위한 for문입니다
        for j in range(N - 2*i):                # 위나 아래로 갈수록 선택하는 블록이 작아지므로 횟수를 줄인다
            answer += arr[start_point - i][j+i] # 중앙을 기준으로 위로 올라가면서 더하기
            answer += arr[start_point + i][j+i] # 중앙을 기준으로 아래로 내려가면서 더하기

    # 중복해서 더해진 가운데 줄 제거
    for i in range(N):
        answer -= arr[start_point][i]

    print(f'#{test_case} {answer}')