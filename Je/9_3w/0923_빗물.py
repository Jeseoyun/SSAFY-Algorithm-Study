H, W = map(int, input().split())
blocks = list(map(int, input().split()))
pre_max = -1
pre_max_idx = -1
total_water = 0

for idx in range(W):
    print(blocks)
    if pre_max == -1:
        pre_max = blocks[idx]
        pre_max_idx = idx
        continue

    # 직전 블록보다 현재 블록이 더 높으면 평탄화 작업 해주기
    if blocks[idx-1] < blocks[idx]:
        # 1) 이전에 가장 높았던 블록보다 현재 블록이 높은 경우
        if pre_max < blocks[idx]:
            # 평탄화 작업 영역 구하기
            h = pre_max - blocks[idx-1]  # 더 낮은 놈의 높이로 맞춰줘야 함
            w = idx - pre_max_idx - 1  # 평탄화 작업 진행할 가로 길이
            print(f"h: {h}, w: {w}")

            total_water += (h * w)

            # 평탄화 한 곳의 높이 갱신
            for renew_idx in range(pre_max_idx+1, idx):
                blocks[renew_idx] = h

            # 가장 높은 지점 갱신
            pre_max = blocks[idx]
            pre_max_idx = idx

        # 2) 현재 블록이 더 낮거나 높이 같은 경우
        else:
            h = blocks[idx] - blocks[idx-1]
            w = idx - pre_max_idx - 1
            print(f"h: {h}, w: {w}")
            total_water += (h * w)

            for renew_idx in range(pre_max_idx+1, idx):
                blocks[renew_idx] = blocks[renew_idx] + h

print(blocks)
print(total_water)