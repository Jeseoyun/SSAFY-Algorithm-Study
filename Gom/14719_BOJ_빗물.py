# 14719 빗물
# 시간초과 

import sys
input = sys.stdin.readline

H,W=map(int,input().split())
H_lst=list(map(int,input().split()))
lst=[[0]*len(H_lst) for _ in range(max(H_lst))]  # 가로 길이: H_lst 원소 길이 / 세로 길이: H_lst 최대값

ans=0

# 빗물 matrix
for j in range(len(lst[0])):  # 열
    for i in range(len(lst)): # 행
        step=0 
        H=H_lst[j] # 높이 정보
        while True:
            if step==H:
                break
            else:
                lst[max(H_lst)-1-step][j]=1
                step+=1

# for k in range(len(lst)):
#     print(lst[k])


# 카운트 함수
for i in range(len(lst)):
    flg=False q
    sub_cnt=0
    for j in range(len(lst[0])):
        # 벽일 때
        if lst[i][j]==1:
            # 앞에 벽이 안세워져 있다면 벽 세워줌. 벽이 있다면 sub_cnt만큼 ans 추가 + sub_cnt 0 초기화
            if flg==False:
                flg=True
            else:
                ans+=sub_cnt
                sub_cnt=0

        # 빈공간일 때
        else:
            if flg==True:
                sub_cnt+=1
            
print(ans)
<<<<<<< HEAD
   
=======


########################################
########################################

# PASS 코드

H, W = map(int, input().split())
H_lst = list(map(int, input().split()))

ans = 0

# 각 인덱스를 기준으로, 왼쪽과 오른쪽에서 가장 높은 벽의 높이를 저장하는 리스트
left_max = [0] * W  
right_max = [0] 

# 왼쪽에서 가장 높은 벽 계산
left_max[0] = H_lst[0] 
for i in range(1, W): 
    left_max[i] =  max(left_max[i - 1],H_lst[i])

# 오른쪽에서 가장 높은 벽 계산
right_max[W - 1] = H_lst[W - 1]
for i in range(W - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], H_lst[i])

# 각 위치에서 빗물이 고일 수 있는 양 계산
# 자신보다 왼쪽으로 높은 벽과 오른쪽으로 높은 벽 중 더 작은 벽과 현재 벽의 높이차의 누적합 YO
for i in range(W):
    ans += min(left_max[i], right_max[i]) - H_lst[i]

print(ans)
>>>>>>> e3f03d82d0a6696d0e508510c97ffbbd438ed55a
