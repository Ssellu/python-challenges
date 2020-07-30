"""
    2. Up & Down 게임 만들기
    - 컴퓨터는 1 ~ 1000 중 임의의 정수 1개를 뽑습니다.
    - 사용자는 컴퓨터가 뽑은 정수를 맞출 때까지 정수를 계속 입력 합니다.
      정답 > 입력값 의 경우 : 'Up!' 출력
      정답 < 입력값 의 경우 : 'Down!' 출력
    - 시도횟수가 15회 미만이라면 "승리!"를, 그렇지 않으면 "패배.." 를 출력하세요.
    (정답이 입력될 때까지 프로그램은 종료되지 않는 것으로 가정합니다.)

"""
import random

correct = random.randint(1, 1000)
cnt = 1
print('진짜 정답 : ', correct)
while True:
    user = int(input('답 : '))
    if correct < user:
        print("DOWN")
    elif correct > user:
        print("UP")
    else:
        print("CORRECT!")
        break
    cnt += 1

# 방법1
# if cnt < 15:
#     print('승리!')
# else:
#     print('패배')

# 방법2
print('승리!' if cnt < 15 else '패배')
