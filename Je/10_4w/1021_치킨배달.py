# (r, c) => 1부터 시작
# 1: 집, 2: 치킨집
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합

# 일부 치킨집 폐업
# - 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개
# - 최대 M개의 치킨집을 고르고, 나머지는 모두 폐업
# - 도시의 치킨 거리가 가장 작게 되도록 -> 치킨 거리의 최솟값 출력
# - 최대 M개 고르라고 했지만 치킨 거리는 무조건 양수이므로 M개 골랐을 때 최솟값 나옴

# 1. 집들의 치킨 거리 구하기 -> BFS
# 2. 각 치킨 집이 몇 개의 집이 치킨 거리를 구하는 대상으로 하는지 구하기
# 3. 치킨집 상위 M개에 대해 치킨 거리 합 최솟값 구하기
# - **치킨집 폐업시키고 나면 각 집의 치킨 거리가 변한다**


import copy
from collections import defaultdict, deque

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def nearest_chicken(city_map, map_size, sx, sy):
    visited = copy.deepcopy(city_map)
    visited[sx][sy] = -1  # 방문 체크: -1

    queue = deque([(sx, sy, 0)])

    while queue:
        x, y, chicken_distance = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size:
                continue
            if visited[nx][ny] == -1:  # 이미 방문한 경우
                continue

            if city_map[nx][ny] == 2:  # 치킨집 발견
                return (nx, ny), chicken_distance + 1

            queue.append((nx, ny, chicken_distance + 1))
            visited[nx][ny] = -1

    return (-1, -1), -1  # error


def main():
    N, M = map(int, input().split())
    city_map = [list(map(int, input().split())) for _ in range(N)]

    house = defaultdict(int)  # {집의 좌표: 치킨 거리}
    chicken = defaultdict(list)  # {치킨 집의 좌표: 집의 좌표}

    # 집들의 치킨 거리 구하기
    # 치킨 거리 = 맨해탄 거리 = bfs 이동 경로의 길이
    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1:
                (cx, cy), cd = nearest_chicken(city_map, N, i, j)  # 치킨 집의 좌표, 치킨 거리

                house[(i, j)] = cd
                chicken[(cx, cy)].append((i, j))

    print(house, chicken)

    # 폐업 시키지 않을 치킨집 M개 선정
    survived_chicken = [k for k, v in sorted(chicken.items(), key=lambda x: len(x[1]), reverse=True)[:M]]
    print(survived_chicken)

    # 도시의 치킨 거리 구하기
    city_chicken_distance = 0
    for chicken_pos in survived_chicken:
        for house_pos in chicken[chicken_pos]:
            city_chicken_distance += house[house_pos]

    print(city_chicken_distance)


if __name__ == "__main__":
    main()