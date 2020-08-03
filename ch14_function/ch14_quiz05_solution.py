"""
    함수명 : calc
    인자 : 정수 2개, 단어 1개
    하는 일 :
        인자로 들어온 단어가 +, -, *, /, %, **, // 인 경우
            해당 단어에 따른 연산 수행
        그 외
            '잘못된 기호'를 출력 후
            연산 결과는 0
    리턴 : 연산 결과

"""
# 함수 정의는 이곳에
def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '**':
        return n1 ** n2
    if op == '/':
        return n1 - n2
    if op == '//':
        return n1 // n2
    if op == '%':
        return n1 % n2
    print('잘못된 기호')
    return 0


# 테스트는 이곳에
b = int(input('정수 1:'))
a = int(input('정수 1:'))
c = input('연산 기호:')
print(f'결과 :{calc(a, b, c)}')
