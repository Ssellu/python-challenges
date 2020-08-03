"""
    사용자에게 소괄호만으로 구성된 문자열을 입력 받습니다.
        이때, 괄호의 짝꿍이 올바른지 True/False 를 출력하세요.
        예) )))()()((( => False
            ()()()()()) => False
            ()(())()()  => True
            ))(())(( => False
            ()(()))( => False
            ((())()) => True
        (위 6개의 테스트를 모두 통과해야합니다.)

"""

s = input('괄호 : ')
lst = list(s)
print(lst)

t = 0
for p in lst:
    if p == '(':
        t += 1
    elif p == ')':
        t -= 1
    if t < 0:
        break
if t == 0:
    print(True)
else:
    print(False)
