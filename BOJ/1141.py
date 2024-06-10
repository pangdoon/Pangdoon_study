N = int(input())

words = []
for _ in range(N):
    word = input()
    words.append(word)

new_words = list(set(words))  # 알아서 중복 제거

new_words.sort(key = len)   # 쉽게하기 위해서 글자순으로 정렬

jub_words = []
for i in range(0, len(new_words)-1):
    flag = 0
    first_word = new_words[i][:]
    for j in range(i+1, len(new_words)):
        seconds_word = new_words[j][:len(first_word)]
        if first_word == seconds_word:
            jub_words.append(first_word)
            flag = 1
        if flag == 1:
            break

print(len(new_words)- len(jub_words))