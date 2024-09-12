from collections import deque


def comb(arr, N, idx, curr, combs):
    if len(curr) == 7:  # 7명이 되면 조합을 저장
        combs.append(curr[:])
        return

    if idx == N**2:
        return

    comb(arr, N, idx+1, curr+[arr[idx]], combs)
    comb(arr, N, idx+1, curr, combs)


def check_YDS(seats, pos):
    cnt = 0
    for x, y in pos:
        if seats[x][y] == "S":
            cnt += 1
        if cnt >= 4:
            return True

    return False


def main():
    N = 5
    seats = [list(input()) for _ in range(N)]

    # 1. 25C7의 조합을 구한다
    groups = []
    comb([i for i in range(N ** 2)], N, 0, [], groups)  # (0~24)까지의 정수 리스트로 조합 구함

    # 2. 각 조합에서 조건 만족하는지 확인
    # - 모두 연결되어 있는지 (bfs로 탐색)
    # - 이다솜파가 4명 이상인지
    res = 0
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for group in groups:
        pos = [(elem // N, elem % N) for elem in group]  # 좌표로 변환

        queue = deque([pos[0]])
        visited = set()
        cnt = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if (nx, ny) in visited:
                    continue
                if (nx, ny) not in pos:
                    continue

                queue.append((nx, ny))
                visited.add((nx, ny))
                cnt += 1

        if cnt == 7 and check_YDS(seats, pos):
            res += 1

    print(res)


if __name__ == "__main__":
    main()
