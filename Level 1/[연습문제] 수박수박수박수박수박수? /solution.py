def solution(n):

    answer = '수'

    while len(answer) < n:
        
        # [ 풀어쓰기 ]
        # if answer[-1] == "수":
        #     answer += "박"
        # else :
        #     answer += "수"

        # [ 한 줄로 간단히 ]    
        answer += "박" if answer[-1] == "수" else "수"

    # print(answer)
    
    return answer