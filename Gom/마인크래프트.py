# 18111 마인크래프트 BOJ

# 초반 생각

'''
왜 실버인데 ..? 


일단.

인벤토리에서 꺼내어 올리는 것(2초)보다 깍는 것(1초) 더 이득

그럼 무조건 깍는게 좋냐? NO 

CASE 별로 모든 경우를 따져서 가장 적게 드는 방법을 고려해야 할듯 

############### 

## CASE

1. ONLY 깍기
2. ONLY 매꾸기
3. 깍기 + 매꾸기 -> HELL 


## CASE 1

가장 낮은 지점까지 전부 깍아버린다. 


## CASE 2

가장 높은 지점까지 전부 매꾼다. 단, 초기 인벤토리 개수가 매꿔야하는 개수 이상이여야 가능


## CASE 3

언제 매꾸는게 최고의 이득일까 

- CASE 3 경우의 수를 어떻게 따져야 할지 모르겟음 


###############

일반화 시켜서 생각해보자.

- 가장 높은 층의 칸들을 전부 깍는 시간과, 가장 낮은 층의 칸들을 전부 매꾸는(단, 개수 조건 만족) 시간을 비교
  >> 더 작은 쪽으로 진행 

- 진행하다가 높이가 같다면 종료하면 됨 

''' 

# 생각 1 코드 구현하다 아닌거 같음을 직감 

'''
N,M,B=map(int,input().split())

lst=[]

for _ in range(N):
    lst.append(list(map(int,input().split())))


flattened_list = [item for sublist in lst for item in sublist]

while True:
    
    # 평탄화 확인
    flattened_list = [item for sublist in lst for item in sublist]
    if len(set(flattened_list))==1:
        break

    H_height=max(flattened_list) # 가장 높은 곳 높이
    L_height=min(flattened_list) # 가장 낮은 곳 높이

    H_cnt=max(H_height)
    L_cnt=min(L_height)

    # 가장 낮은 곳을 인벤토리 상자로 못 매꾸는 경우, 무조건 깍아야 함
    if B<L_cnt:
        # 가장 높은 곳 전부 1로 깍음
        # 근데 이게 맞냐 ? 코드 ㅈㄴ 복잡하잖아 ,, 딱 봐도 시간초과 GooD
    
    else:
        # 매꿨을 때와 깍았을 때 비교
        # ㅋㅋ ,, 


'''



###############################

## 뇌리에 스친 생각

'''

1차원 리스트라고 생각한다면, 

가장 낮은 지점과 높은 지점 사이에 높이에 대해 모든 연산을 수행해보고, 그 중 가장 작은거 뽑으면 되지 않나 ,, ?

- 개수가 모자라다면 그 높이는 만들 수 없으므로 그냥 넘어가면 됨 
- 500*500 연산

'''


N,M,B=map(int,input().split())
ans_S=0
ans_H=0

lst=[]

for _ in range(N):
    lst.append(list(map(int,input().split())))


# 높은 것 부터 깍아서 B 다 채워주고, 올려줄거임 
flattened_list = sorted([item for sublist in lst for item in sublist],reverse=True)
#print(flattened_list)

# 체크 리스트
# 딕셔너리에 개수를 담아서 연산하고, SET으로 만든다면 시간 복잡도 줄어드려나 ?? 

check_num=[] # 중복 높이의 경우 넘어감

for i in range(len(flattened_list)):
    if flattened_list[i] in check_num:
        continue
    else:
        sub_S=0
        sub_H=0

        cur_H=flattened_list[i]
        for j in range(len(flattened_list)):
            # 같은 좌표거나 높이가 동일한 경우 처리 넘어감
            if i==j or flattened_list[i]==flattened_list[j]:
                pass 
            
            else:
                if flattened_list[j]>flattened_list[i]:
                    B+=flattened_list[j]-flattened_list[i]
                    sub_S+=flattened_list[j]-flattened_list[i]
                
                # 차이 만큼 인벤토리에서 가져와 씀, 근데 음수가 되면 만들 수 없는 높이이므로 넘어감 
                else:
                    B-=flattened_list[i]-flattened_list[j]
                    sub_S+=(flattened_list[i]-flattened_list[j])*2

                    if B<0:
                        break

        # 탈출 안되고 끝까지 돌았다면 (for else 구문)        
        else:
            if ans_S>sub_S:
                ans_S=sub_S
                ans_H=sub_H


print(ans_S,ans_H) 

# 전부 0 출력 된다 GOOD 
# BREAK TIME ,, 