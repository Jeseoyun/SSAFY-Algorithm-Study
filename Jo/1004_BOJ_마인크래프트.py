N, M, B = map(int,input().split())
block = []
for _ in range(N):
    # 각 줄의 입력을 받아 리스트로 변환한 후 block 리스트에 추가
    block.append([int(x) for x in list(map(int, input().split()))])

# 가능한 최소 시간을 저장하기 위한 변수 ans
ans = int(1e9)
# 최종 블록 높이를 저장할 변수
glevel = 0

for i in range(257):
    # 사용할 블록 수와 가져올 블록 수
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            # 현재 블록의 높이가 목표 높이 i보다 높으면,
            # 해당 블록에서 얼마나 많은 블록을 가져올 수 있는지 계산하여 take_block에 더함
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                #현재의 블록의 높이가 목표 높이 i보다 낮으면,
                #목표 높이에 도달하기 위해 필요한 블록 수를 계산해서 use_block에 더함
                use_block += i - block[x][y]

    # 만약 필요한 블록 수(use_block)가 가져올 수 있는 블록 수와 주어진 블록 수(B)의 합보다 크면, 
    # 현재 높이를 건너뛰고 다음 높이로 진행
    if use_block > take_block + B:
        continue

    # 전체 시간 계산
    count = take_block * 2 + use_block

    # 현재 계산된 시간이 기존의 시가보다 작다면, 시간 업데이트 및 높이 재설정
    if count <= ans:
        ans = count
        glevel = i

print(ans, glevel)

