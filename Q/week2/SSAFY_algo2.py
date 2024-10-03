'''
다익스트라 알고리즘으로 진행 예정
while 이동방향에 벽이 없다면 계속 진행
dfs
일단 진행?
1. 벽에 부딪힐 때 까지 한칸씩 앞으로
2. 한칸씩 앞으로 가면서 vis를 최소거리로 갱신 안에 있는 값들을 갱신 해줌 min 값으로
3. 앞에 벽이 있다 이 때 DFS 진행  (stack에 값 삽입)
4. 못 가는 곳이면 어떻게 처리하지..? => flag 세워서 stack 빠져나왔는데 flag가 안세워졌다 = 탈출 실패

이 문제의 핵심은 한칸한칸 확인하는 것이 아닌 벽에 부딪힐 때까지 이동하는 것이 핵심이였던 것 같습니다.
벽에 부딪히거나 범위를 벗어날 때까지 이동방향만큼 진행한 후 DFS를 진행하고 vis에 최단거리를 작성하는 방식으로 진행했습니다
'''

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def main():
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        # 기본 입력 받는 과정
        n, m = map(int, input().split())                                #행과 열
        arr = [list(map(int, input().split())) for _ in range(m)]       # 배열
        st_i, st_j, de_i, de_j = map(int, input().split())

        vis = [[float('inf')] * n for _ in range(m)]                    # 최소거리를 저장 vis를 생성 및 초기화하였습니다.
        flag = False                                                    # 탈출에 성공했는지 여부를 판단해주는 변수입니다
        answer = 0                                                      # answer입니다

        stack = [(st_i, st_j)]                                          # 스택에 출발지 값 넣고
        vis[st_i][st_j] = 0                                             # vis값 0으로 초기화해줍니다

        while stack:                                                    # 스택 안에 값이 있을 경우
            cur_x, cur_y = stack.pop()                                  # 현재 x,y 좌표를 pop

            for i in range(4):                                          # 진행할 수 있는 4 방향 체크를 진행합니다
                nx = cur_x                                              # 아래 while문에서 계속 증가시키기 위해 cur_x의 값을 nx에 복사했습니다
                ny = cur_y                                              # 위와 같은 이유로 ny에 cur_y의 값을 복사했습니다
                count = 0                                               # 이동거리는 현재 0입니다

                while not (nx + dx[i] < 0 or nx + dx[i] >= n or ny + dy[i] < 0 or ny + dy[i] >= m) and arr[nx + dx[i]][ny + dy[i]] != 1:
                    # 코드가 더럽지만 이렇게 안하면 안풀려요...
                    # 만일 진행방향으로 한칸 옮겼을 때 not (범위 벗어났다) and 한칸 옮긴 칸이 벽은 아닌지 체크하고 둘 다 만족할 시 
                    nx += dx[i]                                         # nx를 진행방향으로 증가
                    ny += dy[i]                                         # ny를 진행방향으로 증가
                    count += 1                                          # 한칸 진행했으니 진행 count를 1 올려줍니다  # 벽을 만나거나 범위를 벗어나기 직전까지 계속 옮겨줍니다

                if nx < 0 or nx >= n or ny < 0 or ny >= m:              # nx나 ny가 범위를 벗어난 경우 아래 코드 무시
                    continue
                if vis[nx][ny] <= vis[cur_x][cur_y] + count:            # 도착할 칸에 적혀있는 거리보다 현재 내가 이동하는 거리가 더 큰 경우 갈 이유가 없기에 아래 코드 무시
                    continue
                if arr[nx][ny] != 0:                                    # 길이 아닐 경우 아래 코드 무시
                    continue

                if nx == de_i and ny == de_j:                           # 만약 도착 목표에 도달한 경우
                    flag = True                                         # flag를 세우고
                    answer = vis[cur_x][cur_y] + count                  # 답을 작성하고
                    break                                               # 탈출합니다 주석을 적으면서 생각했는데 flag 없이 탈출했는데 stack에 값이 남아있으면 flag가 true인 경우와 같은 것 같습니다
                                                                        # 안써도 될 변수를 사용했군요

                vis[nx][ny] = vis[cur_x][cur_y] + count                 # 위의 경우 다 안걸렸을 경우 vis를 최소거리로 갱신해주고
                stack.append((nx, ny))                                  # 스택에 값을 넣어줍니다

        if flag:
            print(f'#{test_case} {answer}')
        else:
            print(f'#{test_case} -1')


if __name__ == '__main__':
    main()