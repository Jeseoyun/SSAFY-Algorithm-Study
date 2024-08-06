import sys
# import json
sys.stdin = open('input.txt.', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(input())
    arr = [x for x in arr if x!= ',']
    # arr = json.loads(input().strip())

    # 깊이 변수
    depth = 0

    # 스택으로 계산할 리스트
    stack_arr = []

    # 계산된 결과 저장 변수
    result = 0

    # 입력 값 순차적 접근
    for i in arr:
        # print(i)

        # 값이 '['이면 스택 추가 및 depth + 1 
        if i == '[':
            stack_arr.append(i)
            depth += 1

        # 값이 ']'이면 stack_arr의 끝 값 부터 '['까지 pop하고 계산, '[' 이면 pop하고 계산 멈춤
        elif i == ']':
            for j in stack_arr[::-1]:
                if j != '[':
                    num = stack_arr.pop()
                    result += int(num) * depth
                    # print(f'{result} {num} * {depth}')
                else:
                    stack_arr.pop()
                    break
            depth -= 1
        
        # 숫자들 스택에 추가
        else:
            stack_arr.append(i)

        # 깊이가 0 되면 계산 종료
        if depth == 0:
            print(f"#{test_case} {result}")