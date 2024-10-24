from collections import deque

def main():
    #방문처리는?
    #배열이 안되니까 set으로?
    #경로를 알 필요는 없는 최단경로? => BFS
    start, end = map(int, input().split())
    visited = set()
    total_dist = 0

    q = deque([])

    q.append((start, 0))
    visited.add(start)

    while q:
        cur_x, cur_dist = q.popleft()

        if cur_x == end:
            total_dist = cur_dist
            break

        temp = []
        temp.append(cur_x + 1)
        temp.append(cur_x - 1)
        temp.append(cur_x * 2)

        for next in temp:
            if next < 0 or next > 100000:
                continue
            if next in visited:
                continue
            
            q.append((next, cur_dist+1))
            visited.add(next)


    print(total_dist)

if __name__ == "__main__":
    main()