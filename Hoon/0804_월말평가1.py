import json
import sys
sys.stdin = open("input.txt", "r")

sum_val = 0

def Calc(input_li, depth):
    global sum_val

    for elem in input_li:
        if isinstance(elem, list):
            Calc(elem, depth+1)
        elif isinstance(elem, int):
            sum_val += elem * depth

def main():
    global sum_val
    test_case = int(input())
    for tc in range(1, test_case+1):
        sum_val = 0
        num = int(input())
        #strip을 써도 중간 공백이 사라지는 건 아님
        #print(input().strip())

        input_li = json.loads(input().strip())
        #print(input_li)

        for elem in input_li:
            if isinstance(elem, list):
                Calc(elem, 2)
            elif isinstance(elem, int):
                sum_val += elem

        print(f"#{tc} {sum_val}")
        
    

if __name__ == "__main__":
    main()