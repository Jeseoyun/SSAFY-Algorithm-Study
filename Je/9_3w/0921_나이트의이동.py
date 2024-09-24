'''
문제 링크: https://www.acmicpc.net/problem/7562
완전탐색 -> bfs or dfs
도착 지점까지의 최소 경로 찾기(이동 경로 정보가 필요없음) -> bfs로 탐색하자
'''


from collections import deque


dxy = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2), (1, -2), (-1, -2)]


def move_knight(board_size, start, destination):
    # 시작 지점과 도착 지점이 같을 경우 움직이지 않아도 됨 (early return)
    if start == destination:
        return 0

    # bfs를 이용해 도착 지점까지 최소 이동 횟수 구하기
    queue = deque()
    visited = set()

    queue.append((start, 0))  # (현재 좌표, 이동 횟수)
    visited.add(start)

    while queue:
        (x, y), cnt = queue.popleft()

        for dx, dy in dxy:
            nx, ny, cnt = x + dx, y + dy, cnt+1  # 말이 1회 이동했으므로 cnt 1 증가

            # 다음 이동 지점이 보드 크기를 벗어난 경우
            if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size:
                continue

            # 다음 이동 지점이 이미 방문한 곳일 경우
            if (nx, ny) in visited:
                continue

            # 다음 이동 지점이 도착 지점일 경우
            if (nx, ny) == destination:
                return cnt

            queue.append(((nx, ny), cnt))
            visited.add((nx, ny))


def main():
    T = int(input())

    for _ in range(T):
        board_size = int(input())  # 체스 보드 크기
        start = tuple(map(int, input().split()))
        destination = tuple(map(int, input().split()))

        min_move_cnt = move_knight(board_size, start, destination)
        print(min_move_cnt)


if __name__ == '__main__':
    main()