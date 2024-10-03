import json
# import sys
# sys.stdin = open("algo1_sample_in.txt", "r")


# 조 선생님 참고

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    costs = json.loads(input().strip())
    total=0

    def dfs(costs,depth):
        global total

        for sub in costs:
            if isinstance(sub,int):
                total+=sub*depth
            else:
                dfs(sub,depth+1)

    dfs(costs,1)
    print(f'#{tc}',total)
