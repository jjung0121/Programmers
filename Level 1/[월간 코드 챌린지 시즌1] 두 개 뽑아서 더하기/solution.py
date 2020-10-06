def solution(numbers):
    
    answer = []
    # print(numbers)
    # print(len(numbers))
    # print(numbers[0]+numbers[1])
    # print(type(numbers[0]+numbers[1]))
    
    for idx, start in enumerate(numbers):
        stop = idx+1
        # print("start = %d" % idx)
        # print("stop = %d" % stop)

        while stop < len(numbers):
            answer.append(numbers[idx]+numbers[stop])
            answer = sorted(set(answer))
            # print("answer = {} ".format(answer))
            stop += 1

    return answer