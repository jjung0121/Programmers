def solution(arr):
    
    answer = []
    
#     # [방법 1] for문을 활용하여 최소값 직접 구하기   
#     min = arr[0]
    
#     if len(arr) > 1:
#         for i in arr[1:]:
#             if min > i:
#                 min = i
#         arr.remove(min)
#         answer = arr
        
#     else :
#         answer.append(-1)

    # [방법 2] min 함수 활용하여 최소값 구하기
    if len(arr) > 1:
        arr.remove(min(arr))
        answer = arr
    else:
        answer = [-1]
    
    return answer