def solution(a, b):

    answer = 0
    # print("a={}, b={}".format(a,b))
    
    if a <= b:
         for i in range(a, b+1):
            # print("b가 크다")
            # print(i)
            answer += i
            # print(answer)
    else:
        for i in range(a, b-1, -1):
            # print("a가 크다")
            # print(i)
            answer += i
            # print(answer)
    
    return answer