def solution(num):
    
    answer = 0
    
    #[ 방법 1 : While문 활용] - 정확도 error 발생
    # while answer < 500:
        # print("while start")
        # num = int(num/2) if num % 2 == 0 else int((num*3)+1)
        # answer += 1 
        # print(answer, num)
        # if num == 1:
            # break
                
    # if num != 1:
        # answer = -1
        
 #=================================================================

    #[ 방법 2 : for문 활용] - success
    for i in range(0, 501):
        if num == 1:
            break
        else:
            num = int(num/2) if num % 2 == 0 else int((num*3)+1)
            answer += 1    
    if num != 1:
        answer = -1    
            
    return answer