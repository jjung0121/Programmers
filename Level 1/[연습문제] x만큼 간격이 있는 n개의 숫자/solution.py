def solution(x, n):
    
    if x > 0:
        answer = list(range(x,x*n+1,x))
    elif x < 0:
        answer = list(range(x,x*n-1,x))
    else: # test8번 runtime error 발생 => x가 0인 경우 로직 추가 필요
        answer = [0 for i in range(n)]
    
    return answer