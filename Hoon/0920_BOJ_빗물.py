def main():
    height, width = map(int, input().split())
    wall_arr = list(map(int , input().split()))
    result = 0

    for check_height in range(height):#높이가 0인경우, 1인경우...
        start_idx = -1
        end_idx = -1
        wall = 0
        #벽이 두개 이상이면서 길이에서 벽의 갯수를 뺀다
        for idx in range(width):
            if wall_arr[idx] > check_height: #벽이 있으면
                wall += 1
                if start_idx == -1:
                    start_idx = idx
                else:
                    end_idx = idx
            
        if wall >= 2:
            result += (end_idx - start_idx + 1) - wall
        

    
    print(result)



if __name__ == "__main__":
    main()