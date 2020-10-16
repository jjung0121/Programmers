def solution(seoul):
    
    # 표현 1
    # position = seoul.index("Kim")
    # return "김서방은 %d에 있다" % position

    #표현 2
    return "김서방은 {}에 있다".format(seoul.index("Kim"))