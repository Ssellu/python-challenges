"""
    1. 사용자가 -1 을 입력할 때까지 정수를 계속 입력 받고 이들의 총합을 출력하세요. (while 문)
"""

s = 0
while True:
    n = int(input('정수(종료는 -1):'))
    if n == -1:
        break
    s += n
    print(f'현재 총합 : {s}')
print(f'최종 총합 : {s}')
