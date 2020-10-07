def solution(s):
    
    s = s.lower()
    y_count, p_count = 0, 0
    
    for i in s:
        if i == "y":
            y_count += 1
        if i == "p":
            p_count += 1
    
    # print("y={},p={}".format(y_count, p_count))
    
    if y_count == p_count:
        answer = True
    else:
        answer = False

    return answer