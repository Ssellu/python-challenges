"""
    - 밑의 각 변수 var 가 지역변수인지 전역변수인지 주석에 기입하세요.

    - 21번줄에 왜 에러가 발생했는지 추론하여 설명하세요.

    - func3()이 전역변수의 var 를 100으로 변경할 수 있도록 코드를 수정하세요.

"""

var = 10  # ______


def func1():
    print(var)  # ______


def func2():
    var = 100   # ______
    print(var)  # ______


def func3():
    print(var)  # ______
    var = 100   # ______

func1()  # 10
func2()  # 100
func3()  # # UnboundLocalError: local variable 'var' referenced before assignment
print(f'전역변수 var 의 값 : {var}')  # 이곳에 100이 출력되어야 합니다.
