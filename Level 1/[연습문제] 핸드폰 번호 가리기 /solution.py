def solution(phone_number):
    
    answer = ''

    for i in phone_number[0:-4]:
        answer += "*"
    for j in phone_number[-4:]:
        answer += j
        
    return answer