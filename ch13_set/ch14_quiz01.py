"""

    < 로또 번호 생성기 >
    1. 랜덤하게 1 ~ 45 중 6개의 숫자를 뽑습니다.
    2. 중복 숫자는 없어야 합니다.
    3. 오름차순 정렬을 하여 출력합니다.

"""

# 힌트) 랜덤 수 생성 방법
import random  # 소스 가장 윗줄에 1번만 작성

n = random.randint(1, 45)  # random.randint(시작수, 끝수) : 시작수~끝수에 해당하는 정수 1개를 뽑는다.
m = random.randint(1, 45)  # random.randint(시작수, 끝수) : 시작수~끝수에 해당하는 정수 1개를 뽑는다.
print(n)
print(m)

