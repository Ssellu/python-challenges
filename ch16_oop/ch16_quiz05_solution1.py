"""
    다음 학생들의 정보를 dictionary 에 저장하세요.
    key 는 학번입니다.
    value 는 Student 인스턴스 입니다.

    학번          이름      평균      등급      연락처
    101         홍길동      88       B        010-2222-1231
    102         김길동      92       A        010-2231-1256
    103         김장미      47       F        010-2512-7754
    201         장아름      85       B        010-9966-3512
    202         최영수      74       C        010-1111-3864
"""
class Student:
    def __init__(self):
        self.num = ''
        self.name = ''
        self.avg = 0
        self.grade = 'F'
        self.contact = ''

s0 = Student()
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()

s0.num = '101'
s0.name = '홍길동'
s0.avg = 88
s0.grade = 'B'
s0.contact = '010-2222-1231'


s1.num = '102'
s1.name = '김길동'
s1.avg = 92
s1.grade = 'A'
s1.contact = '010-2231-1256'


s2.num = '103'
s2.name = '김장미'
s2.avg = 47
s2.grade = 'F'
s2.contact = '010-2512-7754'


s3.num = '201'
s3.name = '장아름'
s3.avg = 85
s3.grade = 'B'
s3.contact = '010-9966-3512'


s4.num = '202'
s4.name = '최영수'
s4.avg = 74
s4.grade = 'C'
s4.contact = '010-1111-3864'


students = dict()
students[s0.num] = s0
students[s1.num] = s1
students[s2.num] = s2
students[s3.num] = s3
students[s4.num] = s4

print(students)

for k, v in students.items():
    print(f'학번 : {k}')
    print(f'이름 : {v.name}')
    print(f'평균 : {v.avg}')
    print(f'등급 : {v.grade}')
    print(f'연락처 : {v.contact}')
    
    