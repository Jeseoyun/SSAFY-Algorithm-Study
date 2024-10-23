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


from collections import deque

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def log(arr):
    for lst in arr:
        for elem in lst:
            print(elem, end=" ")
        print()
    print()


def get_chicken_distance(map_size, sx, sy, survived_chicken):
    visited = [[0]*map_size for _ in range(map_size)]
    visited[sx][sy] = 1  # 방문 체크

    queue = deque([(sx, sy, 0)])

    while queue:
        # log(visited)
        x, y, chicken_distance = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size:
                continue
            if visited[nx][ny] == 1:  # 이미 방문한 경우
                continue

            if (nx, ny) in survived_chicken:  # 치킨집 발견
                return chicken_distance + 1

            queue.append((nx, ny, chicken_distance + 1))
            visited[nx][ny] = 1


def get_comb(arr, max_comb_size, idx, comb, combs):
    if len(comb) > max_comb_size:
        return

    if idx == len(arr):
        if not comb:
            return

        combs.append(comb)
        return combs

    get_comb(arr, max_comb_size, idx+1, comb+[arr[idx]], combs)  # 현재 값 포함
    get_comb(arr, max_comb_size, idx+1, comb, combs)  # 현재 값 미포함


def main():
    N, M = map(int, input().split())
    city_map = [list(map(int, input().split())) for _ in range(N)]

    houses = []
    chickens = []

    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1:
                houses.append((i, j))
            if city_map[i][j] == 2:
                chickens.append((i, j))

    # 1. 치킨집 중에서 최대 M개를 고르기
    # - 가능한 경우의 수를 모두 찾기 위해 조합 사용
    chicken_combs = []
    get_comb(chickens, M, 0, [], chicken_combs)

    # 2. 최소 치킨 거리 구하기
    min_chicken_dist = float('inf')
    for survived_chicken in chicken_combs:
        total_dist = 0
        for house in houses:
            pos_x, pos_y = house
            total_dist += get_chicken_distance(N, pos_x, pos_y, survived_chicken)
        min_chicken_dist = min(min_chicken_dist, total_dist)

    print(min_chicken_dist)


if __name__ == "__main__":
    main()
