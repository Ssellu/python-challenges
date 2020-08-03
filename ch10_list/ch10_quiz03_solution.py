"""
    다음 이차원 리스트 lst 를 사용하여 다음과 같이 출력되도록 이차원 for 문을 구성하세요.

    (1)
    1   2   3   4
    5   6   7   8
    9   10  11  12
    13  14  15  16

    (2)
    1   5   9   13
    2   6   10  14
    3   7   11  15
    4   8   12  16

    (3)
    1   2   3   4
    8   7   6   5
    9   10  11  12
    16  15  14  13

"""
lst = [[m + n for n in range(1, 5)] for m in range(0, 14, 4)]

print('---- 가로 방향 출력 ----')
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end='\t')
    print()


print('---- 세로 방향 출력 ----')
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[j][i], end='\t')
    print()

print('---- 지그재그 방향 출력 ----')
for i in range(len(lst)):

    if i % 2 == 0:
        for j in range(len(lst[i])):
            print(lst[i][j], end='\t')
    else:
        for j in range(len(lst[i])):
            print(lst[i][3-j], end='\t')
    print()
"""

    가로 10칸, 세로 10칸으로 구성된 이차원리스트 map 이 있습니다.
        1) 사용자에게 행, 열 인덱스를 입력 받고 해당 위치를 기준으로
        가로, 세로, 대각선 방향의 모든 원소를 1 증가하세요.
        2) 수정된 map 을 10 X 10 정사각형의 형태로 출력하세요.
                for n in map:
                    for m in n:
                        print(f'{m:4}', end='')
                    print()
        
        3) 사용자가 -1 을 입력하기 전까지 (1),(2)를 반복하세요.

"""

map = [[0 for n in range(10)] for m in range(10)]
user_r = 0
user_c = 0

while True:
    user_r = int(input('행(종료는 -1):'))
    if user_r == -1:
        break
    user_c = int(input('열:'))

    for r in range(10):
        for c in range(10):
            if user_r == r or \
                    user_c == c or \
                    user_c + user_r == c + r or \
                    user_c - user_r == c - r:
                map[r][c] += 1

    # 방법1. 간단하게 보여주기
    for n in map:
        for m in n:
            print(f'{m:4}', end='')
        print()


    # 방법2. 인덱스를 붙여 보여주기
    # print(f'{" ":4}', end='')
    # for i in range(10):
    #     print(f'{"[" + str(i) + "]":4}', end='')
    # print()
    # a = 0
    # for n in map:
    #     print(f'{"[" + str(a) + "]":4}', end='')
    #     for m in n:
    #         print(f'{m:4}', end='')
    #     print()
    #     a += 1
