"""
    - 밑의 각 변수 var 가 지역변수인지 전역변수인지 주석에 기입하세요.

    - 21번줄에 왜 에러가 발생했는지 추론하여 설명하세요.
        => func3() 내부의 var 에 대입(=)이 이루어지면서 인터프리터는 이 var 를 전역이 아닌 지역변수로 인식한다.
           이때 지역변수는 최초 대입이 이루어지는 시점에 생성되므로 그 보다 앞선 print()를 실행하는 시점에서
            지역 var는 존재하지 않는다. 따라서 'local variable 'var' referenced before assignment' 가 출력된다.

    - func3()이 전역변수의 var 를 100으로 변경할 수 있도록 코드를 수정하세요.
       func3() 가장 상단에
        'global var' 를 기입한다. (28줄 참고)

"""

var = 10  # 전역


def func1():
    print(var)  # 전역


def func2():
    var = 100   # 지역
    print(var)  # 지역


def func3():
    global var
    print(var)  # 지역
    var = 100   # 지역

func1()  # 10
func2()  # 100
func3()  # # UnboundLocalError: local variable 'var' referenced before assignment
print(f'전역변수 var 의 값 : {var}')  # 이곳에 100이 출력되어야 합니다.
