"""

    < 로또 번호 생성기 >
    1. 랜덤하게 1 ~ 45 중 6개의 숫자를 뽑습니다.
    2. 중복 숫자는 없어야 합니다.
    3. 오름차순 정렬을 하여 출력합니다.

"""

import random
lotto_set = set()
while len(lotto_set) != 6:
    lotto_set.add(random.randint(1, 45))

lotto = list(lotto_set)
lotto.sort()
print(lotto)


