# 14719 빗물


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
   