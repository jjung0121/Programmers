def solution(s):
    answer = ''
    word_list = s.split(" ")

    for idx1, word in enumerate(word_list):
        change_word = ""
        
        for idx2, w in enumerate(word):
            if idx2 % 2 == 0:
                # print("짝수",idx, w)
                change = w.upper()
            else:
                # print("홀수",idx, w)
                change = w.lower()

            change_word += change
        word_list[idx1] = change_word
    answer = " ".join(word_list)
        
    return answer