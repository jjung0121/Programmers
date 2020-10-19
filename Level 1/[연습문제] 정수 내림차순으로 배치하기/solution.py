# [ 방법 1 ] for문 활용하여 풀어쓰기
# def solution(n):

#     answer = ""
    
#     for i in sorted(list(str(n)),reverse=True):
#         answer += i
#     answer = int(answer)
    
#     return answer


# [ 방법 2 ] join 활용하여 간략히
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))