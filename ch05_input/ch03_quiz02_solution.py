"""

 2. 사용자의 몸무게와 키를 입력 받아 BMI 지수를 출력하세요.
    BMI = 체중(kg)/(신장(m)^2)
    BMI 지수는 소숫점 1자리까지만 출력하세요.

    몸무게 : 50
    키 : 150
    BMI : 22.2

"""

weight = int(input("몸무게:"))
height = int(input("키:")) / 100

bmi = weight / height ** 2
print(f'BMI : {bmi}')
