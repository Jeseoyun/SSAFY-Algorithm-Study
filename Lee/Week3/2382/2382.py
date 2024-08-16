import sys
sys.stdin = open('sample_input.txt', 'r')
import pprint

T = int(input())

dxy = [[0,0], [0,1], [0,-1],[-1,0], [1,0]]

def move_turn(move):
    if move == 1:
        return 2
    elif move == 2:
        return 1
    elif move == 3:
        return 4
    elif move == 4:
        return 3

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    misangmool = {}

    #미생물[x, y 좌표] = [미생물 수, 이동방향]
    for idx in range(len(arr)):
        misangmool[arr[idx][0],arr[idx][1]] = arr[idx][2], arr[idx][3]

    # print(misangmool)
    vacine = []

    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1:
                vacine.append([i,j])
            else:
                if j == 0 or j == N-1:
                    vacine.append([i,j])

    temp_list = []

    for _ in range(0, K):
        for key, items in list(misangmool.items()):
            x, y = key
            k, move = items[0], items[1]

            # 본인 방향에 맞게 이동
            nx, ny = x + dxy[move][0], y + dxy[move][1]

            # 이동 좌표가 이미 있으면
            if [nx, ny] in temp_list:
                # 미생물이 더 많은 군집 확인
                if misangmool[nx, ny][0] < misangmool[x, y][0]:
                    print(f"{x,y} -> {nx, ny} 이동 좌표가 더 커서 합쳐짐")
                    misangmool[nx,ny] = misangmool[nx,ny][0] + k, misangmool[nx,ny][1]
                    del misangmool[(x,y)]
                else:
                    print(f"{x,y} -> {nx, ny} 내 군집이 더 커서 합쳐짐")
                    misangmool[nx,ny] = misangmool[nx,ny][0] + k, misangmool[x,y][1]
                    del misangmool[(x,y)]
            else:
                temp_list.append([nx, ny])
                print(f"{x,y} -> {nx, ny} 좌표 없어서 리스트 추가후 이동")
                # print(temp_list)
                misangmool[nx,ny] = k, move
                del misangmool[(x,y)]

            # vacine 구역에 들어오면
            if [nx, ny] in vacine:
                # 미생물 절반 죽었을때 1이상이면 갱신
                if k //2 > 0 :
                    # 반대 방향
                    print(f"{x,y} -> {nx, ny} 영역와서 꺾음")
                    move = move_turn(move)
                    misangmool[nx, ny] = k//2, move
                # 죽음
                else:
                    print(x,y, "죽음")
                    del misangmool[(x,y)]
        temp_list = []
        pprint.pprint(misangmool)
    
    result = 0
    for value in misangmool.values():
        result += value[0]
    
    print(result)