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

    def __init__(self, num='', name='', avg=0, grade='F', contact=''):
        self.num = num
        self.name = name
        self.avg = avg
        self.grade = grade
        self.contact = contact

    # solution2 에서 print_info() 추가 : 모든 정보 출력
    def print_info(self):
        print(f'학번 : {self.num}')
        print(f'이름 : {self.name}')
        print(f'평균 : {self.avg}')
        print(f'등급 : {self.grade}')
        print(f'연락처 : {self.contact}')


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
   v.print_info()
