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

    def print_info(self):
        print(f'학번 : {self.num}')
        print(f'이름 : {self.name}')
        print(f'평균 : {self.avg}')
        print(f'등급 : {self.grade}')
        print(f'연락처 : {self.contact}')


# solution3 에서 객체를 튜플화 한 후 딕셔너리로 재구성

t = (Student('101', '홍길동', 88, 'B', '010-2222-1231'),
     Student('102', '김길동', 92, 'A', '010-2231-1256'),
     Student('103', '김장미', 47, 'F', '010-2512-7754'),
     Student('201', '장아름', 85, 'B', '010-9966-3512'),
     Student('202', '최영수', 74, 'C', '010-1111-3864'))

students = dict()
for st in t:
    students[st.num] = st

print(students)

for k, v in students.items():
    v.print_info()
