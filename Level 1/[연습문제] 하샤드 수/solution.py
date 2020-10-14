def solution(x):

    # [ 방법 1 ] - runtime error 발생
    # first, second = map(int, str(x))
    
    ## 표현 1. 풀어쓰기
    # if x % (first + second)  == 0:  
    #     answer = True        
    # else :
    #     answer = False 
    
    ## 표현 2 one line
    # answer = True if x % (first + second)  == 0 else False 
    
    #============================================================
    
    # [ 방법 2 : 매개변수 길이 확인하여 분기시키는 로직 추가 ] - runtime error 발생
    # if len(str(x)) >= 2:
    #     first, second = map(int, str(x))
    #     answer = True if x % (first + second)  == 0 else False
    # else:
    #     answer = True
        
    #============================================================
    
    # [ 방법 3 :for 문을 활용한 매개변수 자릿수 합 산출]-  success
    
    total = 0

    for i in str(x):
        total += int(i)
        answer = True if x % total == 0 else False
            
    return answer