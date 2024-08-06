import sys, json
sys.stdin = open('algo1_sample_in.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    # 유지보수 비용의 요소 수
    N = int(input())
    # 각각의 비용을 문자열로 입력
    costs = json.loads(input().strip())
    # 총 비용 0으로 초기화
    total_cost = 0

    # 총 비용 계산 함수
    # 주어진 리스트 내 원소들을 순회하며 자료형이 int에 해당할 경우 depth를 곱하여 total_cost에 더함
    # 자료형이 list에 해당한다면 해당 원소에 대하여 depth를 1씩 늘려나가며 연산
    def count_cost(lst, depth):
        global total_cost
        for elem in lst:
            if isinstance(elem, int):
                total_cost += elem * depth
            else:
                count_cost(elem, depth + 1)

    #입력된 리스트와 깊이 1을 인자로 받음
    count_cost(costs, 1)

    print(f'#{test_case} {total_cost}')


