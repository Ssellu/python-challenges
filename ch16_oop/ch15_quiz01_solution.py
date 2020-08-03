"""
    Pokemon 클래스 만들기
        필드 : 이름(name), 레벨(level), 체력(hp)
        메서드 : X

"""
class Pokemon:
    def __init__(self):
        self.name = ''
        self.level = 0
        self.hp = 0

"""
    위에서 정의한 Pokemon 클래스를 사용하여 
    Pokemon 객체를 3개를 생성하고, 
    각 객체들의 이름은 input() 으로 입력 받고
    level 은 1 ~ 100 중 랜덤하게 
    hp 는 level 의 100배로 저장하세요.
    
    위에서 저장된 3개 객체의 모든 정보를 출력하세요.

"""
import random

p0 = Pokemon()
p1 = Pokemon()
p2 = Pokemon()

p0.name = input('1번 포켓몬 이름:')
p1.name = input('2번 포켓몬 이름:')
p2.name = input('3번 포켓몬 이름:')


p0.level = random.randint(1, 100)
p1.level = random.randint(1, 100)
p2.level = random.randint(1, 100)

p0.hp = p0.level
p1.hp = p1.level
p2.hp = p2.level

print(f'{p0.name} / LV.{p0.level} / HP.{p0.hp}')
print(f'{p1.name} / LV.{p1.level} / HP.{p1.hp}')
print(f'{p2.name} / LV.{p2.level} / HP.{p2.hp}')
