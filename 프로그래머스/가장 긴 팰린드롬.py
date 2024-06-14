def solution(word):
    answer = 0


    max_count = 1

    for word_index in range(len(word)):
        count = 1

        left = -1  # 왼쪽 포인터
        right = 1  # 오른쪽 포인터
        while True:
            if word_index + left >= 0 and word_index + right <= len(word):

                if word[word_index + left] == word[word_index + right]:
                    count += 2
                    left -= 1
                    right += 1
                else:
                    break


    return answer

word = "abcdcba"

solution(word)