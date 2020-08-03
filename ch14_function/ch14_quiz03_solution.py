"""
    함수명 : get_random_pokemon()
    인자 : 없음
    하는 일 :
        "피카츄", "라이츄", "파이리", "꼬부기", "버터풀" 중 1개의 단어를 랜덤하게 고르기
    리턴 : 포켓몬 이름

"""

def get_random_pokemon():
    import random
    return random.choice(("피카츄", "라이츄", "파이리", "꼬부기", "버터풀"))



# 테스트는 이곳에
print(f'{get_random_pokemon()}')
