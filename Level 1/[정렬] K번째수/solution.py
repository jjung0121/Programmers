def solution(array, commands):

    answer = []
    
    for each in commands:
        i, j, k = each
        print("i={}, j={}, k={}". format(i,j,k))
        new_array = sorted(array[i-1:j])
        print("new_array = %s" % new_array)
        
        for idx, value in enumerate(new_array):
            if idx == k-1:
                answer.append(value)
                print(answer)
    
    return answer