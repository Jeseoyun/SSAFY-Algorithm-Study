import sys, json
sys.stdin = open('algo1_sample_in.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    # 유지보수 비용의 요소 수
    N = int(input())
    # 각각의 비용을 문자열로 입력
    costs = json.loads(input().strip())
    total_cost = 0

    def count_cost(lst, depth):
        global total_cost
        for elem in lst:
            if isinstance(elem, int):
                total_cost += elem * depth
            else:
                count_cost(elem, depth + 1)

    count_cost(costs, 1)

    print(f'#{test_case} {total_cost}')


