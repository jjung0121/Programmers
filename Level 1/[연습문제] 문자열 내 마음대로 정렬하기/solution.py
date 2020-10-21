def solution(strings, n):
    
    answer = sorted(strings, key = lambda x : x[n]) 
    # (x[n], x)) # x[n] 이후  x 기준을 추가하여 같은 문자일 경우 사전순 정렬 조건 추가
    
    return answer