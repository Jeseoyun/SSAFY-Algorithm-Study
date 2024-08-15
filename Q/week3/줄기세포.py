'''
BFS로 풀려다가 실패
현재 고려해야할 것 k에 도달했을 경우 종료 어떻게?
cur_time만 가지고는 어떻게 2에서 시작한 애들 체크를 어떻게 할 것인가
결국 우선순위 q를 써야한다 or cur_time에 cur_val만큼 더해서 stack에 때리면 
결국 그 아이가 실행되는 시점의 cur_time = 진행된 시간이 된다를 이용해 보기


'''

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_dict = {}
    stack = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                arr_dict[(i, j)] = arr[i][j]
                stack.append((i, j, arr[i][j], 0))

    while stack:
        cur_x, cur_y, cur_val, cur_time = stack.pop()
        if cur_time == k:
            stack.append(cur_x, cur_y, cur_val, cur_time)
            break

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if arr_dict[(nx, ny)] > cur_val or arr_dict[(nx, ny)] == 0:
                continue

