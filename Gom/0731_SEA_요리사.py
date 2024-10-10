'''
풀이법

1. 재료를 2 세트로 나눈다

2. 나눈 재료 2세트에 대해 각각 요리사가 재료 2개를 선택할 수 있는 조합

3. 최소가 되게 하는 합 구하기 


* 문제 설명 애매함
- 2개로 나눈 각 세트 안에서 따진 조합 중 각각의 차가 아니라, 세트에서 나눈 조합 자체의 차였음 ,,

'''


import itertools

T=int(input())
for tc in range(1,T+1):
        
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]

    ans=1e9

    # 재료 번호
    ingredient_num=[x for x in range(N)]

    # 음식 조합 리스트
    foods_comb_lst=itertools.combinations(ingredient_num, N//2)

    # A 조합이 foods_comb_lst 였다고 생각하고 접근
    # A를 기준으로 없는 원소를 따져 B 조합 원소 추출 
    for a_food_lst in foods_comb_lst:   # A조합 중 하나를 받아옴
        b_food_lst=[]

        for num in ingredient_num:
            if num not in a_food_lst:   # A를 선택하고 남은 B조합 재료 추가
                b_food_lst.append(num)


        
        # A,B 각각의 세트에서, 2개를 선택해서 만들 수 있는 모든 경우의 수 연산
        a_synergy_lst=itertools.combinations(a_food_lst,2)
        b_synergy_lst=itertools.combinations(b_food_lst,2)

        # A 시너지 합
        a_synergy_sum=0
        for a_synergy in a_synergy_lst:
            # (i,j) + (j,i)
            i,j=a_synergy
            a_synergy_sum+=lst[i][j]+lst[j][i]


        # B 시너지 합
        b_synergy_sum=0
        for b_synergy in b_synergy_lst:
            # (i,j) + (j,i)
            i,j=b_synergy
            b_synergy_sum+=lst[i][j]+lst[j][i]

        ans=min(ans,abs(a_synergy_sum-b_synergy_sum))
        
    print(f'#{tc}',ans)

