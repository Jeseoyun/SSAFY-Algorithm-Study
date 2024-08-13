# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
import sys
import pprint
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N) ]

    sepo = {}
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # 생명력 0인애는 없는애임
            if arr[i][j] > 0:
                # 세포 좌표 = [생명력, 개인시간, 활성여부, 생사(True 살아있음, False 죽음)]
                sepo[i, j] = [arr[i][j], 0, False, True]

    # print(type(sepo[0,0][0]))

    dxy = [[0,1], [0,-1], [1,0], [-1,0]]

    for time in range(K):
        # print(time)
        # pprint.pprint(sepo)
        for key in list(sepo.keys()):
            # 살아 있으면
            if sepo[key][3]:
                # 생명력과 개인시간이 같을때
                if sepo[key][0] == sepo[key][1]:
                    # 활성 상태 ON
                    sepo[key][2] = True
                    
                    #본인 좌표
                    x, y = key

                    # 번식
                    for dx, dy in dxy:
                        nx, ny = dx + x, dy + y
                        # 번식할 좌표가 sepo dict에 없거나 있으면 본인 값보다 작으면서 안죽은 상태이고 활성화 중이아니면 번식
                        if (nx, ny) not in sepo.keys() or (sepo[(nx, ny)][0] < sepo[key][0] and sepo[(nx, ny)][3] and not sepo[(nx, ny)][2]):
                            sepo[nx, ny] = [sepo[key][0], 0, False, True]

                # 생명력 다쓰고 죽을때 (기다린 시간 - 생명시간 == 생명시간)
                if sepo[key][3] and sepo[key][1] - sepo[key][0] == sepo[key][0]:
                    # 활성 OFF
                    sepo[key][2] = False
                    # 죽음
                    sepo[key][3] = False

            sepo[key][1] += 1

    # 살아있는 줄기세포 확인
    for key in sepo:
        if sepo[key][3]:
            count += 1
    
    print(count)
