"""

 1. 두 정수를 입력 받고 큰 수를 출력하세요.
    만약 두 정수가 같으면 "같음" 을 출력하세요.
"""
# a = int(input("정수1:"))
# b = int(input("정수2:"))
# if a > b:
#     print(f'첫 번째 정수가 더 크다. ({a})')
# elif a < b:
#     print(f'두 번째 정수가 더 크다. ({b})')
# else:
#     print('두 수는 같다.')

"""
 2. 정수 1개를 입력 받고 2, 3, 5의 배수인 지 각각 판별하세요.
    14 : 2의 배수
    15 : 3의 배수 5의 배수
    30 : 2의 배수 3의 배수 5의 배수
    17 : 해당 사항 없음

      => 위와 같은 텍스트로 출력하세요.
"""
n = int(input('정수:'))

if n % 2 == 0:
    print('2의 배수')
if n % 3 == 0:
    print('3의 배수')
if n % 5 == 0:
    print('5의 배수')
if n % 2 and n % 3 and n % 5:  # n % 2 != 0     n % 2
    print('해당 사항 없음')

"""
 3. 국, 영, 수 각 3과목의 점수를 입력 받고
    평균을 소숫점 2자리까지 출력하세요.
    평균에 따른 학점을 출력하세요.
    "합격" 혹은 "불합격" 을 출력하세요.

    - 학점 기준
    평균이 90 점 이상 : A
    80점 이상 ~ 90점 미만 : B
    70점 이상 ~ 80점 미만 : C
    60점 이상 ~ 70점 미만 : D
    60점 미만 : F

    - 합격 기준
    평균 85점 이상, 세 과목 모두 70점 이상

"""
kr = float(input('국:'))
en = float(input('영:'))
ma = float(input('수:'))
avg = (kr + en + ma) / 3

grade = 'F'
pass_ = avg >= 85 and kr >= 70 and en >= 70 and ma >= 70

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'


if pass_:
    print('합격')
else:
    print('불합격')
print(f'평균 : {avg:.2f}점')


"""
 4. 놀이동산에 놀이기구가 4개 있습니다.
    나이와 키를 입력 받아 탑승 가능한 놀이기구의 이름과 개수를 출력하세요.
    (개수는 cnt = 0 을 활용하세요.)
     회전목마 : 80cm 이상 200cm 미만
     유령의집 : 15세 이상, 110 cm 이상
     롤러코스터 : 13세 이상 60세 미만, 140 cm 이상
     자이로드롭 : 10세 이상, 130 cm 이상

"""
cnt = 0
age = int(input('나이:'))
height = float(input('키:'))
if 80 <= height < 200:
    print('회전목마')
    cnt += 1
if age >= 15 and height >= 110:
    print('유령의 집')
    cnt += 1
if 13 <= age < 60 and height >= 140:
    print('롤러코스터')
    cnt += 1
if age >= 10 and height >= 130:
    print('자이로드롭')
    cnt += 1
print(f'총 {cnt}개 탑승 가능')









