from collections import deque

def main():
    size = int(input())
    word = input()

    queue = deque(list(word))
    original_queue = deque(list(word))

    loop_cnt = 0

    # 사이클이 발생할 때까지 회전
    while True:
        loop_cnt += 1
        new_queue = deque([])
        temp_queue = deque([])

        for i in range(len(queue)):
            if i % 2 == 0 or i == len(queue) - 1:
                new_queue.append(queue.popleft())
            else:
                temp_queue.appendleft(queue.popleft())

        while temp_queue:
            new_queue.append(temp_queue.popleft())
        
        # 원래 상태로 돌아왔으면 종료
        if new_queue == original_queue:
            break

        queue = new_queue

    # 필요한 횟수만큼 회전
    cnt = size % loop_cnt
    queue = deque(list(word))

    for _ in range(cnt):
        new_queue = deque([])
        temp_queue = deque([])

        for i in range(len(queue)):
            if i % 2 == 0 or i == len(queue) - 1:
                new_queue.append(queue.popleft())
            else:
                temp_queue.appendleft(queue.popleft())

        while temp_queue:
            new_queue.append(temp_queue.popleft())

        queue = new_queue

    # 결과 출력
    new_word = "".join(list(queue))
    print(new_word)

def main2():
    size = int(input())
    word = input()
    # size가 너무 큼.

    loop_cnt = 0

    word_li = list(word)
    temp_li = list(word)
    next_li = []

    while True:
        loop_cnt += 1
        next_li = []
        length = len(temp_li)
        for i in range(length):
            if i % 2 == 0 or i == length - 1:
                next_li.append(temp_li[i])
        for i in range(length-1, 0, -1):
            if i % 2 == 0 or i == length - 1:
                continue
            next_li.append(temp_li[i])
        temp_li = next_li

        # print(temp_li, next_li)

        if word_li == temp_li:
            break

    cnt = size % loop_cnt
    
    next_li = []
    for _ in range(cnt):
        next_li = []
        length = len(temp_li)
        for i in range(length):
            if i % 2 == 0 or i == length - 1:
                next_li.append(temp_li[i])
        for i in range(length-1, 0, -1):
            if i % 2 == 0 or i == length - 1:
                continue
            next_li.append(temp_li[i])
        temp_li = next_li

    next_str = "".join(temp_li)
    print(next_str)

if __name__ == "__main__":
    main2()