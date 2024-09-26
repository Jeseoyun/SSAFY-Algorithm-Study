import json


def restore_campus(costs, calculated_cost, depth=1):
    # 기저조건: 리스트가 아닌 정수형일 경우
    # -> depth와 유지보수 비용을 곱하여 저장하고 재귀 종료
    if isinstance(costs, int):
        calculated_cost += [costs * depth]
        return
    else:
        # 정수형이 아니라 리스트일 경우
        # 반복문을 통해 탐색 대상을 다시 순회하고 재귀함수 호출
        for cost in costs:
            restore_campus(cost, calculated_cost, depth+1)


def main():
    T = int(input())

    for test_case in range(1, T+1):
        N = int(input())  # 유지보수 비용의 요소 수
        costs = json.loads(input().strip())  # 유지보수 비용 리스트

        calculated_cost = []  # 유지보수 비용을 계산하여 저장
        restore_campus(costs, calculated_cost)

        print(f"#{test_case} {sum(calculated_cost)}")


if __name__ == "__main__":
    main()