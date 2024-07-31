# 2805 농작물 수확하기

# 수익계산 함수
def farm_area(lst,mid):

    # cnt: 센터 기준 추가 폭 / revenue: 수익
    cnt=0
    revenue=0

    for i in range(N):
        row_lst=lst[i]
        
        # 행이 절반보다 작을 때: cnt 1씩 추가
        if i<mid:
            revenue += sum(row_lst[mid - cnt:mid + cnt + 1])
            cnt+=1
        
        # 행이 절반 보다 같거나 클 때: cnt 1씩 감소
        else:
            revenue += sum(row_lst[mid - cnt:mid + cnt + 1])
            cnt -= 1

    return revenue


T=int(input())
for tc in range(1,T+1):
    # 행 높이
    N=int(input())
    
    # 농장 입력
    lst=[list(map(int,input())) for _ in range(N)]
    
    # 수익 계산
    # mid -> N//2 
    ans=farm_area(lst,N//2) 
    print(f'#{tc}',ans)