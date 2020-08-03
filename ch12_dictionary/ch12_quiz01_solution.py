"""
    < 영단어장 만들기 >
    영단어는 key, 그의 뜻은 value 로 두는 dictionary 를 만드세요.
    메뉴)
        1. 단어 등록
        2. 단어 검색
        3. 모든 단어 보기
        4. 퀴즈 풀기
        0. 종료하기

        1. 단어 등록
            새 영단어와 그의 뜻을 입력 받고 dictionary 에 추가합니다.

        2. 단어 검색
            영단어를 입력 받아 그의 뜻을 출력합니다.
            미등록된 단어인 경우 '미등록 단어'를 출력합니다.

        3. 모든 단어 보기
            현재 등록되어있는 모든 단어와 뜻을 출력합니다.

        4. 퀴즈 풀기 (선택문제)
             컴퓨터는 랜덤하게 영어 단어를 선택합니다.
             해당 단어의 뜻을 문제로 내고, 사용자에게 답을 입력 받습니다.
             정답 혹은 땡 을 출력합니다.

        0. 종료하기

"""

menu = '''1. 단어 등록
2. 단어 검색
3. 모든 단어 보기
4. 퀴즈 풀기
0. 종료하기'''

# 빈 딕셔너리를 만든다. (반복문 안에 넣지 않는다!)
wordbook = {}

while True:
    print(menu)
    select = input('선택:')
    if select == '0':
        break
    elif select == '1':
        w = input('새 단어:')
        m = input(f'{w}의 뜻:')
        wordbook[w] = m
    elif select == '2':
        w = input('검색할 단어:')
        if w in wordbook:
            print(f'{w} : {wordbook[w]}')
        else:
            print('미등록 단어')
    elif select == '3':
        for w, m in wordbook.items():
            print(f'{w} : {m}')
    elif select == '4':

        # ** 랜덤 단어 고르기 **
        # 방법1 - 랜덤한 인덱스를 활용하는 방법
        # key(단어)로만 구성된 튜플을 만든다. (리스트도 상관없다.)
        words = tuple(wordbook.keys())

        # 랜덤한 인덱스를 하나 뽑는다.
        import random
        idx = random.randrange(len(words))

        # 고른 인덱스를 사용하여 영단어를 랜덤하게 뽑는다.
        # 딕셔너리는 인덱스가 없기때문에 튜플을 만든 것이다.
        w = words[idx]

        # 해당 단어를 key로 가진 원소의 value(뜻)을 문제로 낸다
        answer = input(f'{wordbook[w]}(은)는 영어로? : ')

        # 방법2 - random.choice() 를 활용하는 방법
        # import random
        # w, m = random.choice(tuple(wordbook.items()))
        # answer = input(f'{m}(은)는 영어로? : ')

        # 정답 여부를 확인한다.
        if answer == w:
            print('정답!')
        else:
            print('땡..')
    else:
        print('잘못 입력하셨습니다.')