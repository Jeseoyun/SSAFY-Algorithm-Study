'''
X 범위가 1,000,000,000네?
그대로 반복문 돌리면 무조건 터지겠네..

반복문을 돌렸을 때 똑같은 단어가 반복되면 더 돌릴 필요 없으니
결과값을 저장할 list를 만들고
나중에 횟수로 카운트해서 결과값 도출

'''


def shuffle():
    global word, word_lst

    new_word = ''
    mid = len(word)//2
    
    #앞뒤로 하나씩 붙여주기
    for i in range(mid):
        new_word += word[i] + word[len(word)-1-i]

    #홀수면 가운데 값 마지막에 더해주기
    if len(word) % 2 == 1:
        new_word += word[len(word)//2]

    word = new_word

X = int(input())
word = input()
start_word = word
word_lst = [word]

while True:
    shuffle()
    if word == start_word:
        break
    word_lst.append(word)

word_lst = word_lst[::-1]
print(word_lst[(X-1) % len(word_lst)])

