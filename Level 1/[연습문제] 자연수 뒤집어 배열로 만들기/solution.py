def solution(n):
    
    # [방법 1] for문으로 직접 바꾸기
#     answer = list(range(0,len(str(n))))
#     replace_index = -1
    
#     for i in str(n):
#         answer[replace_index] = int(i)
#         replace_index -= 1

    # [방법 2] reverse 함수 활용
    answer = list(map(int, reversed(str(n))))
    
    return answer