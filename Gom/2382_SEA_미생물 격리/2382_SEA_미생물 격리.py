'''

[구현 목표]

1. 모서리 도달하면 개체수 절반 만들기 + 방향 반대로 돌리기

2. 좌표 겹쳐지면 미생물 수 더해주기 + 방향 결정 해주기


[내 생각]

- 각각의 미생물을 한번 이동할 때마다, 전체를 탐색한다면 시간 복잡도 높을 수도? 미생물 좌표들에 대해서만 처리?


[질문]

- 겹쳐지는 좌표 처리 어떻게 해줘야 할까?
- 기존 좌표 정보를 날리는 문제점 발생  

>> matrix 접근 (x)
>> 미생물 좌표 집합들에 대해서만 처리해주기 (o)

'''


# main
T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())
    arr=[]
    for _ in range(K):
        i,j,num,dir=map(int,input().split())
        dir-=1
        arr.append([i,j,num,dir])


    # 1~4: 상,하,좌,우 
    dij=[(-1,0),(1,0),(0,-1),(0,1)]

    # 반전 인덱스
    rev_dij=[1,0,3,2]

    # M시간 동안 이동
    for _ in range(M):

        # i,j: 좌표 / num: 개체 수 / dir: 방향
        for i in range(len(arr)):
            arr[i][0]+=dij[arr[i][3]][0]  # arr[i][3] => dir
            arr[i][1]+=dij[arr[i][3]][1]

            # 미생물이 모서리로 이동했다면?
            if arr[i][0]==0 or arr[i][0]==N-1 or arr[i][1]==0 or arr[i][1]==N-1:
                arr[i][2]//=2
                arr[i][3]=rev_dij[arr[i][3]]
            
        arr.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)

        # i=1 ~ len(arr)-1
        i=1
        while i<len(arr):
            # 좌표(i,j) 같음 -> num 값 병합, i행 삭제 
            if arr[i-1][0:2]==arr[i][0:2]:
                arr[i-1][2]+=arr[i][2]
                arr.pop(i)
            else:
                i+=1

    ans=0
    for i in range(len(arr)):
        ans+=arr[i][2]

    print(f'#{tc}',ans)



    
    

            
            

























