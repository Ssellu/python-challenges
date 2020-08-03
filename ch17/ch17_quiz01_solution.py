"""
    다음 클래스 Pokemon 에는 랜덤한 이름 뽑기를 위하여 이름 리스트가 있습니다.
    random_names = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

    1. 이를 클래스 변수로 선언하고,

    2. 이 리스트를 활용하여 랜덤한 이름을 뽑아
    뽑힌 이름을 return 하는 @staticmethod 를 정의하여

    3. 아래 코드의 에러가 없어지도록 하세요.


"""
import random


class Pokemon:
    random_names = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

    def __init__(self):
        self.name = Pokemon.get_random_name()

    @staticmethod
    def get_random_name():
        return random.choice(Pokemon.random_names)


print(f'그냥 뽑아 보기 : {Pokemon.get_random_name()}')
print(f'그냥 뽑아 보기 : {Pokemon.get_random_name()}')
print(f'그냥 뽑아 보기 : {Pokemon.get_random_name()}')

p0 = Pokemon()
p1 = Pokemon()
print(f'p0.name : {p0.name}')
print(f'p1.name : {p1.name}')
