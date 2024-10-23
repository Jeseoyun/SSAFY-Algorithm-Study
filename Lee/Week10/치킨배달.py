# # https://www.acmicpc.net/problem/15686 치킨배달
# # 집, 치킨집 위치 확인
# # 집 별로 치킨집 거리 계산 거리 제일 작은 값으로
# # 치킨집 최대 M개 선택 가능 ( 조합으로 만들어 보자 )
import itertools

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken_house = []
house = []

# 집과 치킨집 위치 확인
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken_house.append((i, j))

# 최소 거리
min_house_chicken_dist = float('inf')

# 치킨집 조합 생성
for chicken_combination in itertools.combinations(chicken_house, M):
    # 각 집에서 가장 가까운 치킨집까지의 거리 합 계산
    house_chicken_dist = 0

    # 하나의 집 고정, 치킨집 조합에 있는 다른 치킨집들하고 계산해서 가장 가까운 치킨집과의 거리를 총합에 더함
    for h_x, h_y in house:
        min_dist = float('inf')
        for c_x, c_y in chicken_combination:
            house_chicken_dist = abs(h_x - c_x) + abs(h_y - c_y)
            # 집에서 가장 가까운 치킨집 거리 업데이트
            min_dist = min(min_dist, house_chicken_dist)
        house_chicken_dist += min_dist

    # 최소 거리의 합을 업데이트
    min_city_chicken_dist = min(min_house_chicken_dist, house_chicken_dist)

# 결과 출력
print(min_house_chicken_dist)
