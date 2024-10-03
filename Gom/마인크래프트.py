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


# 실패 코드

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
        sub_S=1e9
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

'''


#####################
#####################

# 마크 풀이

'''
- 구현 PBL

- 높이 정보만 유지하고 있으면 되므로 2차원(ground) 1차원(flattened_ground)을 변환해줌 -> only 가독성

- 타겟 높이가 될 수 있는 범위 =  min(flattened_ground) ~ max(flattened_ground)

  >> flattened_ground 각각의 높이를 순회하면서 타겟 높이로 잡고, 최소의 시간이 나오는 높이를 정답으로 정하자  (타겟 높이: 평탄화로 만들고자 하는 높이)
  
  >> 타겟으로 잡은 높이를 만들지 못하는 경우가 존재함

    - 인벤토리 초기 블록 개수(B) + 타겟보다 높아서 깍은 개수(remove_blocks)  - 타겟보다 낮아서 올린 개수(add_blocks) < 0 : 블록이 모자라기 때문에 만들 수 없음 

    - 위의 조건에 걸러지지 않는다면, 현재 저장된 최소 시간과 비교해보고 짧다면 높이, 시간 갱신


[어려웠던 점]

- 타겟으로 1차적으로 리스트를 순회하는데, 다른 높이들과 비교하는 과정에서 시간 복잡도가 높아짐 

- Counter 모듈 사용 
  >> 리스트 원소의 개수를 딕셔너리 형태로 반환해 줌
  >> 중복된 원소들을 순회하지 않고, 딕셔너리 하나만 순회하면 됨

'''

from collections import Counter

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]  

# 땅의 높이를 평탄화(2차원 -> 1차원)해서 리스트로 변환한 후, 높이별 개수를 셈
flattened_ground = [block for row in ground for block in row]
height_count = Counter(flattened_ground)

# 가장 높은 높이, 가장 낮은 높이
min_height = min(flattened_ground)
max_height = max(flattened_ground)

# 최소 시간 무한으로 갱신, 높이 0 초기화
min_time = float('inf')
best_height = 0


# 타겟 높이 순회 : 최소 높이 ~ 최대 높이
for target_height in range(min_height, max_height + 1):
    remove_blocks = 0  # 타겟 보다 높았을 때 제거할 블록
    add_blocks = 0  # 타겟 보다 낮았을 때 올릴 블록
    
    # 높이별 개수를 딕셔너리에 담아놓았기 때문에 바로 차이 계산
    for height, count in height_count.items():
        # 타겟 보다 높이가 큰 블록들 >> 깍아줌, 깍아준 만큼 remove_blocks에 추가
        if height > target_height:
            remove_blocks += (height - target_height) * count
        
        # 타겟 보다 낮은 블록들 >> 더해줌, 더해준 만큼 add_block에 추가
        else:
            add_blocks += (target_height - height) * count

    # 블록 개수 조건을 따져 만들 수 있다면
    # 개수 조건 ) B + removed_blocks < add_blocks  : 기본 블록 + 깍아서 쟁긴 블록 < 추가해야 하는 블록   
    if remove_blocks + B >= add_blocks:
        time = remove_blocks * 2 + add_blocks  # 깍는데 걸리는 시간 2초, 올리는데 걸리는 시간 1초

        # 갱신 조건
        # 1. 시간이 더 작게 걸림 -> 무조건 갱신
        # 2. 시간은 같은데, 높이가 더 큰 경우(문제 명시)
        if time < min_time or (time == min_time and target_height > best_height):
            min_time = time
            best_height = target_height

print(min_time, best_height)
