
"""
    < 무인 호텔 관리 프로그램2 >
    1) 호 개수와 층 개수를 입력 받습니다.
        단, 층과 호는 각 최대 99개 미만으로 가정합니다.
    2) 층 개수 X 방 개수와 같은 길이의 이차원 리스트를 생성합니다.
        3층 5 개 -->
        [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        2층 3 개 -->
        [
            [0,0,0],
            [0,0,0]
        ]
    3) 사용자 메뉴를 메시지로 보여주고 메뉴를 선택 받습니다.
        < 메뉴 >
        1. 체크인
        2. 체크아웃
        3. 현황 보기
        0. 종료하기

        1. 체크인
            방 호수(101번부터 시작)를 입력 받습니다. (1층 1호 : 101, 2층 1호 : 201, ..)
            방이 이미 입실 중이면 "입실 중인 방은 체크인 하실 수 없습니다."를 출력하세요.
            빈 방인 경우 "입실 완료!"를 출력하고 메뉴로 돌아갑니다.
        2. 체크아웃
            방 호수를 입력 받습니다.
            방이 빈 방이면 "빈 방은 체크아웃 하실 수 없습니다."를 출력하세요.
            체크인 상태인 경우 "퇴실 완료!"를 출력하고 메뉴로 돌아갑니다.
        3. '방호수 - 상태'를 출력합니다.
            출력 예)
                101호 : 빈 방
                102호 : 입실 중
                201호 : 입실 중
                202호 : 빈 방
                301호 : 빈 방
                302호 : 입실 중
        0. 종료
            반복을 종료하고 '영업 종료' 를 출력합니다.
    4) 사용자가 메뉴에서 0을 입력할 때까지 (3) 과정을 진행합니다.

"""
# 0. 전체 층/방 개수 입력 받기
floor_num = int(input('층 개수:'))
if floor_num > 99 or floor_num < 0:
    print('층의 개수는 1개 이상 최대 99개까지 가능합니다.')
    exit(0)  # 프로그램 종료
room_num = int(input('방 개수:'))
if room_num > 99 or floor_num < 0:
    print('호의 개수는 1개 이상 최대 99개까지 가능합니다.')
    exit(0)  # 프로그램 종료



# 1. 리스트 만들기 (층:행, 호:열)
# 1-방법1. for 문으로 append()
# hotel = []
# for n in range(floor_num):
#     tmp = []
#     for m in range(room_num):
#         tmp.append(0)
#     hotel.append(tmp)


# 1-방법2. 특수 for 문으로 0을 total 개 채우기
hotel = [[0 for n in range(room_num)] for m in range(floor_num)]

# 2. 각 층/호의 자릿수 구하기
f_digit = 1 if floor_num < 10 else 2
r_digit = 1 if room_num < 10 else 2

# 3. 메뉴 프로그램 시작
menu = '''1. 체크인
2. 체크아웃
3. 현황 보기
0. 종료하기'''
while True:
    print(menu)
    select = input('선택:')
    if select == '1':
        """
        방 호수(101번부터 시작)를 입력 받습니다. (1층 1호 : 101, 2층 1호 : 201, ..)
        방이 이미 입실 중이면 "입실 중인 방은 체크인 하실 수 없습니다."를 출력하세요.
        빈 방인 경우 "입실 완료!"를 출력하고 메뉴로 돌아갑니다.
        """
        num = input('체크인 하실 호수 : ')

        # 층과 호의 인덱스 구하기 (1119호 => 11층 19호 => [10]번 행 [18]번 열)
        f_idx = int(num[:f_digit]) - 1
        r_idx = int(num[-r_digit:]) - 1

        if (f_idx < 0 or f_idx >= floor_num) or (r_idx < 0 or r_idx >= room_num):
            print('잘못된 방 호수입니다. 메뉴로 돌아갑니다.')
            continue
        if hotel[f_idx][r_idx]:
            print('입실 중인 방은 체크인 하실 수 없습니다.')
            continue
        hotel[f_idx][r_idx] = 1
        print('입실 완료!')

    elif select == '2':
        """
        방 호수를 입력 받습니다.
        방이 빈 방이면 "빈 방은 체크아웃 하실 수 없습니다."를 출력하세요.
        체크인 상태인 경우 "퇴실 완료!"를 출력하고 메뉴로 돌아갑니다.
        """
        num = input('체크아웃 하실 호수 : ')
        f_idx = int(num[:f_digit]) - 1
        r_idx = int(num[-r_digit:]) - 1

        if (f_idx < 0 or f_idx >= floor_num) or (r_idx < 0 or r_idx >= room_num):
            print('잘못된 방 호수입니다. 메뉴로 돌아갑니다.')
            continue
        if not hotel[f_idx][r_idx]:
            print('빈 방은 체크인 하실 수 없습니다.')
            continue
        hotel[f_idx][r_idx] = 0
        print('퇴실 완료!')

    elif select == '3':
        s = '---- 객실 현황 ----\n'
        for i in range(floor_num):
            print(f'---- {i+1}층 ----')
            for j in range(room_num):
                print(f'{i+1}{j+1:02}호 - {"입실 중" if hotel[i][j] else "빈 방"}')
            print()

    elif select == '0':
        print('프로그램 종료!')
        break
    else:
        print('잘못된 입력! 다시 입력하세요.')