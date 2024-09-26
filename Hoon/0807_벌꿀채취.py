import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 겹치지 않게 벌통 선택
# 복잡하지만, C 값 이하가 되도록 벌통 선택
# 최대 점수가 되도록 벌통을 선택해야함,
# 점수 계산은 선택한 좌표들의 제곱의 합.

# 두 일꾼이 꿀을 채취하여 얻을 수 있는 수익의 합이 최대

max_sum = 0

def calc_max(arr, cur_idx, size_x, cur_point, max_point, cur_value):
    
    if max_point < cur_point:
        return
    
    global max_sum
    
    if cur_idx >= size_x:
        max_sum = max(max_sum, cur_value)
        return
    
    #안 더하고
    calc_max(arr, cur_idx+1, size_x, cur_point, max_point, cur_value)
    #더하고
    calc_max(arr, cur_idx+1, size_x, cur_point + arr[cur_idx], max_point, cur_value + arr[cur_idx]**2)



def main():
    global max_sum

    for test_case in range(1, T + 1):
        max_score = 0
        num, size_x, max_point = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(num)]

        # print(size_x, max_point)
        # print(board)

        #각 좌표마다 최대값을 저장해두고
        #고르기만 조합으로

        save_arr = [[0]*num for _ in range(num)]

        for y in range(num):
            for x in range(num - (size_x-1)):
                max_sum = 0
                calc_max(board[y][x:x+size_x], 0, size_x, 0, max_point, 0)
                save_arr[y][x] = max_sum

        #디버깅
        for li in save_arr:
            for elem in li:
                print(elem, end=" ")
            print()

        #4중 for문시 100 * 100 이하의 테스트 케이스
        def find_second(first_y, first_x, num, size_x):
            max_second = 0
            for second_x in range(first_x + size_x, num - (size_x-1)):
                max_second = max(max_second, save_arr[first_y][second_x])

            for second_y in range(first_y+1, num):
                for second_x in range(num - (size_x-1)):
                    max_second = max(max_second, save_arr[second_y][second_x])

            return max_second
            
            

        for first_y in range(num):
            for first_x in range(num - (size_x-1)):
                first_value = save_arr[first_y][first_x]

                second_value = find_second(first_y, first_x, num, size_x)

                max_score = max(max_score, first_value+second_value)
                

        print(f"#{test_case} {max_score}")

if __name__ == "__main__":
    main()