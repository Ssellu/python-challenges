"""
    함수명 : get_average()
    인자 : 국, 영, 수
    하는 일 : 세 과목의 평균 구하기
    리턴 : 평균

"""
# 함수 정의는 이곳에
def get_average(kr, en, ma):
    return (kr + en + ma) / 3


# 테스트는 이곳에
print(get_average(88, 77, 66))

k = int(input('국:'))
e = int(input('영:'))
m = int(input('수:'))
print(f'평균 : {get_average(k, e, m)}')
