'''
미로 문제가 나오면 일단 BFS 코드를 구성합니다
BFS 코드의 구조는
dx, dy 만들어 놓기
배열선언을 통한 map 생성
visit 배열 선언
queue 생성
출발점 queue에 push = append
visit에 출발 좌표 등록

while 문 시작
바로 queue pop을 통한 현재 좌표 받아오기
4번 도는 for문 생성
받아온 현재 좌표를 x,y로 선언한 후 dx, dy를 더한 nx, ny 값을 생성
(nx, ny와 dx, dy가 변수가 이름이 비슷하여 헷갈릴 경우 next_x, next_y와 direction_x, direction_y로 생성하는 걸 추천합니다)
if문을 통해 먼저 map의 범위를 벗어나는지 체크
다음 if문을 통해 map에서 길이 맞는지, 방문한 적이 있는지 체크
위의 if문에 걸릴 경우 continue를 통해 아래의 과정은 패스

위의 if문 통과한 값은 정상값이므로
queue에 넣고, visit에 방문 표시를 해줍니다
이때 얼만큼 걸렸는지 알고싶은 경우 visit[nx][ny]에 visit[x][y]의 값에서 1 더한 값을 입력합니다

이렇게 BFS를 생성한 후 문제 조건을 봅니다

조건 1. 출발점은 2로 주어진다 => 단순하게 2중 for문을 통해 출발점의 좌표를 가져왔습니다
조건 2. 도착점은 3으로 주어진다 => 그래서 arr[nx][ny]의 좌표가 3이 될 경우 flag를 세운 후 while문을 종료했습니다.
조건 3. 도착하는지 체크해라 => queue안의 값이 다 빠질 때 까지 flag를 세우지 못 했다면 그 지점은 갈 수 없는 지점입니다
'''

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visit = [[0]*16 for _ in range(16)]                 # 이전 test_case에 사용했던 visit값이 남아 있을 수 있으므로 초기화합니다
    deq = deque()

    start_x = 0
    start_y = 0
    start_point_flag = False

    # start 포인트를 찾는 과정입니다. 위에서 flag를 false로 초기화 했으므로 찾을 때 까지 for문을 돌게되고 찾는 순간 빠르게 빠져 나옵니다
    for i in range(16):
        if not start_point_flag :           # 2. 두 번째 for문을 빠져나오고 첫 번째 for문으로 돌아갔을 때 flag가 세워지므로 첫 번째 for문도 탈출합니다
            for j in range(16):
                if arr[i][j] == 2:
                    start_x = i
                    start_y = j
                    start_point_flag =True
                    break                   # 1. break를 통해 두 번째 for문을 빠져나오고
        else :
            break
    
    # 위와 같이 로직을 구성한 이유는 파이썬에서는 for문이 지정된 횟수만큼 무조건 돈다는 것을 배웠고
    # 그 횟수를 다 돌기 전에 빠져나오고 싶었기 때문입니다

    # BFS 과정입니다
    visit[start_x][start_y] = 1
    deq.append((start_x, start_y))
    
    # 만일 3을 찾을 경우 종료 시키기 위한 flag입니다
    end_point_flag = False
    
    while deq:
        if not end_point_flag:
            #BFS 과정
            cur = deq.popleft()
            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]
                if nx < 0 or nx >= 16 or ny < 0 or ny >= 16:
                    continue
                if visit[nx][ny] or arr[nx][ny] == 1:
                    continue
            
            # 문제 조건인 도착지 도착시 flag를 세워줍니다
                if arr[nx][ny] == 3:
                    end_point_flag = True
                visit[nx][ny] = 1
                deq.append((nx,ny))
        else:
            break

    # 도착지에 도착했는지 안했는지 체크 후 결과를 보여줍니다.
    if end_point_flag :
        print(f'#{test_case} 1')
    else :
        print(f'#{test_case} 0')