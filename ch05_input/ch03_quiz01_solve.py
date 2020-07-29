"""

 1. 사용자의 이름, 태어난 해, 연락처, 주소를 입력 받아 그 결과(이름, 나이, 연락처, 주소)를 출력하세요.

"""
name = input('이름:')
age = 2020 - int(input('생년:')) + 1
tel = input('연락처:')
addr = input('주소:')

print(f"""< {name}님의 정보 >
나이 : {age}세
연락처 : {tel}
주소 : {addr}""")


