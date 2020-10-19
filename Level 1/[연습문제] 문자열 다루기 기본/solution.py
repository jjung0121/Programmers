
# [ 방법 1 ] if문 활용하여 문자열의 길이 및 원소 파악
# def solution(s):
    
#     answer = True
#     number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
#     if len(s) == 4:
#         # print("길이 4")
#         for i in s:            
#             if i not in number:
#                 answer = False
        
#     elif len(s) == 6:
#         # print("길이 6")
#         for i in s:    
#             if i not in s:
#                 answer = False
    
#     else:
#         answer = False
        
#     return answer


# [ 방법 2 ] isdigit() 함수와 in문 활용
def solution(s):
    return s.isdigit() and len(s) in (4,6)