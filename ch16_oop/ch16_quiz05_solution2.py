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
    # solution1 에서 생성자만 고침
    def __init__(self, num='', name='', avg=0, grade='F', contact=''):
        self.num = num
        self.name = name
        self.avg = avg
        self.grade = grade
        self.contact = contact


s0 = Student('101', '홍길동', 88, 'B', '010-2222-1231')
s1 = Student('102', '김길동', 92, 'A', '010-2231-1256')
s2 = Student('103', '김장미', 47, 'F', '010-2512-7754')
s3 = Student('201', '장아름', 85, 'B', '010-9966-3512')
s4 = Student('202', '최영수', 74, 'C', '010-1111-3864')

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
