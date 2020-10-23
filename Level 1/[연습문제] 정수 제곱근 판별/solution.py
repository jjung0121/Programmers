import math

def solution(n):
    
    answer = 0   
    sqrt = str(math.sqrt(n))
    
    if sqrt[-2:] == ".0":
        answer = pow(int(float(sqrt)) + 1, 2)
    else:
        answer = -1
    
    return answer

# [ Troubleshooting ]
# Error Message :at line 9 | print(int(sqrt)+1)
# - alueError: invalid literal for int() with base 11: '11.0'
# Solution
# - str에서 int로 변환하기 전, float으로 먼저 형변화 과정 필요
# Reference
# - https://careerkarma.com/blog/python-valueerror-invalid-literal-for-int-with-base-10/
