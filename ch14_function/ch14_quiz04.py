"""
    함수명 : greet()
    인자 : 이름, 나이
    하는 일 :
        미성년자인 경우 : XX(아)야, 안녕? 를 return
        성인인 경우 : XX님, 안녕하세요? 를 return
    리턴 : 위 둘 중 하나의 문장

"""
# 함수 정의는 이곳에
def greet(name:str, age:int)->str:
    pass



# 테스트는 이곳에
name = input('이름:')
age = int(input('나이:'))
print(greet(name, age))  # None 이 나오면 안됨