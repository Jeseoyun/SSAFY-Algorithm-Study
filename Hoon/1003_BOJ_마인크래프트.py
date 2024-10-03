#7:55 시작
import sys
sys.stdin = open("input.txt", "r")

DEL_BLOCK = 2
CRE_BLOCK = 1

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

def main():
    size_y, size_x, block_num = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size_y)]

    # print_board(board)
    
    time = 0
    height = 0

    min_height = float("inf")
    max_height = float("-inf")

    for li in board:
        for elem in li:
            min_height = min(min_height, elem)
            max_height = max(max_height, elem)
    
    # print(min_height, max_height)
    min_cost = float("inf")
    cost = 0
    for goal_height in range(min_height, max_height+1):
        # print(goal_height)
        cost = 0
        temp_block = block_num
        for li in board:
            for elem in li:
                if goal_height > elem:
                    cost += CRE_BLOCK * (goal_height - elem)
                    temp_block -= (goal_height - elem)
                elif goal_height < elem:
                    cost += DEL_BLOCK * (elem - goal_height)
                    temp_block += (elem - goal_height)

        if temp_block < 0:
            continue
        
        if min_cost > cost:
            min_cost = cost
            height = goal_height
        elif min_cost == cost:
            height = max(height, goal_height)

    time = min_cost

    print(time, height)

    return

if __name__ == "__main__":
    main()