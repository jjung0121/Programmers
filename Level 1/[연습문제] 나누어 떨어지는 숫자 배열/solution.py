def solution(arr, divisor):
    answer = []
    
#     # 표현방법1. 풀어쓰기
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
            
#     if len(answer) == 0:
#         answer.append(-1)
#     else :
#         answer.sort() 

    # 표현방법2. 한 줄로 표현
    [answer.append(i) for i in arr if i % divisor==0]
    [answer.append(-1) if len(answer) == 0 else answer.sort()]

    return answer