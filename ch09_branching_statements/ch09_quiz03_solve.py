"""
    3. 구구단 게임 만들기
        - 사용자에게 판 수를 입력 받으세요
        - 해당 판 수만큼 구구단 문제를 출력하고 답을 입력 받아
          "정답!" 혹은 "땡.."을 출력하세요.
        - 정답률이 60% 이상일 경우 "승리!" 아니면 "패배.."를 출력하세요.
        - 사용자 로그를 출력하세요. (문제, 사용자 답, 실제 정답을 출제된 순서대로)

"""

import random

total = int(input('몇 판? : '))
cnt = 0
log = ''

for n in range(total):
    n1 = random.randint(2, 9)
    n2 = random.randint(1, 9)
    quiz_str = f'{n1} X {n2}'
    user_str = input(f'{quiz_str} = ')
    log += f'{quiz_str} ({user_str}/{n1*n2})\n'

    if int(user_str) == n1 * n2:
        print('정답!')
        cnt += 1
    else:
        print('땡..')

# 방법1.
# if cnt / total >= .6:
#     print('게임 결과 : 승리!')
# else:
#     print('게임 결과 : 패배..')
# print(log)

# 방법2.
print(f'게임 결과 : {"승리!" if cnt / total >= .6 else "패배.."}')
print(log)
