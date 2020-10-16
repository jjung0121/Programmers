def solution(s):
    
    position = int(len(s)/2)
    answer = s[position] if len(s) % 2 == 1 else s[position-1:position+1]
    
    return answer