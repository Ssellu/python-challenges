"""

    < 학생 관리 프로그램 >

    step 1. 다음 학생들의 정보를 dictionary 에 저장하세요.
    key 는 학번입니다.

    학번          이름      평균      등급      연락처
    101         홍길동      88       B        010-2222-1231
    102         김길동      92       A        010-2231-1256
    103         김장미      47       F        010-2512-7754
    201         장아름      85       B        010-9966-3512
    202         최영수      74       C        010-1111-3864
"""
students = {
    '101': {'name': '홍길동', 'avg': 88, 'grade': 'B', 'contact': '010-2222-1231'},
    '102': {'name': '김길동', 'avg': 92, 'grade': 'A', 'contact': '010-2231-1256'},
    '103': {'name': '김장미', 'avg': 47, 'grade': 'F', 'contact': '010-2512-7754'},
    '201': {'name': '장아름', 'avg': 85, 'grade': 'B', 'contact': '010-9966-3512'},
    '202': {'name': '최영수', 'avg': 74, 'grade': 'C', 'contact': '010-1111-3864'},
}

# 각 학년의 마지막 학번을 기록할 딕셔너리를 생성하면 학번을 구하기 편리합니다.
last_nums = {}
print(students.keys())
for k in students:  # k : '101', '102', '103', '201', '202'
    # g: 학년
    g = int(k[0])  # g: 1, 1, 1, 2, 2
    if g in last_nums:  # last_nums 에 학년 키가 있다면
        last_nums[g] += 1  # 해당 value 에 1을 누적
    else:  # 학년이 없다면
        last_nums[g] = 1

print(f'현재 각 학년의 마지막 학번 : {last_nums}')
"""
    step 2. (1)의 딕셔너리에 학생 3명의 정보를 입력 받아 추가 저장합니다.
        - 학생의 이름, 국, 영, 수, 학년, 연락처를 입력 받습니다.
        
        - 학년은 학번의 가장 앞자리에 해당합니다.
          예를 들어 딕셔너리에 저장된 2학년 학생이 4명이라면, 다음 2학년 학생의 학번은 205가 되어야 합니다.

        - 평균은 국,영,수 의 평균을 계산하여 저장합니다.
            *사용자에게 입력 받지 않습니다.

        - 등급은 평균에 따른 A, B, C, D, F 중 하나로 저장합니다.
            *사용자에게 입력 받지 않습니다.
            90 점 이상 : A
            80점 이상 ~ 90점 미만 : B
            70점 이상 ~ 80점 미만 : C
            60점 이상 ~ 70점 미만 : D
            60점 미만 : F
"""

for i in range(3):  # 3회 반복
    small_d = dict()
    small_d['name'] = input('이름:')
    g = int(input('학년:'))
    small_d['contact'] = input('연락처:')
    kr = int(input('국어:'))
    en = int(input('영어:'))
    ma = int(input('수학:'))
    small_d['avg'] = (kr + en + ma) / 3
    if small_d['avg'] >= 90:
        small_d['grade'] = 'A'
    elif small_d['avg'] >= 80:
        small_d['grade'] = 'B'
    elif small_d['avg'] >= 70:
        small_d['grade'] = 'C'
    elif small_d['avg'] >= 60:
        small_d['grade'] = 'D'
    else:
        small_d['grade'] = 'F'

    if g in last_nums:
        last_nums[g] += 1
    else:
        last_nums[g] = 1

    students[f'{g}{last_nums[g]:02}'] = small_d
print('---학생 3명 추가 결과---')
for k, v in students.items():
    print(f'{k}:{v}')

"""
    step 3. 사용자 메뉴를 출력합니다. (선택문제)
        1. 학번으로 검색
        2. 연락처 뒷번호로 검색
        3. 1등 학생 보기
        4. 모든 학생 보기
        0. 종료
"""
menu = '''1. 학번으로 검색
2. 연락처 뒷번호로 검색
3. 1등 학생 보기
4. 모든 학생 보기
0. 종료'''
while True:
    print(menu)
    select = input('선택:')
    if select == '0':
        break

    elif select == '1':
        """
        1. 학번으로 검색
        학번을 입력 받고 해당 학생의 모든 정보를 출력합니다.
        미등록 학번인 경우 '미등록 학번'을 출력합니다.
        """
        num = input('검색 학번:')
        if num in students:
            print(f'{students[num]["name"]}'
                  f'/평균 {students[num]["avg"]}점'
                  f'/학점 {students[num]["grade"]}'
                  f'/{students[num]["contact"]}')
        else:
            print('미등록 학번')
    elif select == '2':
        """
        2. 연락처 뒷번호로 검색
        연락처 뒷번호 4자리를 입력 받아 연락처가 일치하는
        '모든' 학생들의 이름, 학년, 연락처를 출력합니다.
        """
        num = input('검색할 연락처 뒷 4자리:')
        result = False
        for k, v in students.items():
            if v['contact'][-4:] == num:
                print(f'{v["name"]}'
                      f'/{k[0]}학년'
                      f'/{v["contact"]}')
                result = True
        if not result:
            print('검색 결과가 없습니다.')

    elif select == '3':
        """
        3. 1등 학생 보기
        평균을 가지고 1등 학생을 찾아 해당 학생의 학번, 이름, 평균 점수를 출력합니다.
        공동 1등인 경우 학년이 가장 높은 학생을,
        그 중 같은 학년에 공동 1등이 있다면 그 학생들 모두를 출력하세요.
        """

        # 가장 첫 번째 학생을 1등으로 잡습니다.
        keys = tuple(students.keys())
        max_st = keys[0]  # 가장 첫 번째 학생의 학번
        cand = [max_st]  # 같은 학년에 공동 1등이 있다면 그 학생들 모두를 담을 리스트 (일단 가장 앞 학생을 저장하고 시작)
        # 위 세 줄을 다음으로 줄일 수도 있다.
        # cand = [tuple(students.keys())[0]]

        # student 딕셔너리의 모든 학생을 대상으로
        for k, v in students.items():
            if k == cand[-1]:
                continue

            # 평균이 같거나 더 높은 학생을 발견했다면
            if v['avg'] >= students[cand[0]]['avg']:

                # ** students[cand[0]]['avg'] 설명
                #   - cand = ['101', '103'] 인 경우  ==> 1등 학생들은 1학년임을 알 수 있다.
                #   - cand[0] => '101'
                #   - students[cand[0]] => students 딕셔너리에 key 가 '101'인 학생(딕셔너리)
                #           => {'name': '홍길동', 'avg': 88, 'grade': 'B', 'contact': '010-2222-1231'}
                #   - students[cand[0]]['avg'] => 88

                # 학년 혹은 평균이 더 높다면
                if (k[0] > cand[0][0]) or (v['avg'] > students[cand[0]]['avg']):
                    # ** cand[0][0] 설명
                    # 예) cand = ['201', '205'] 가 있을 경우  ==> 1등 학생들은 2학년임을 알 수 있다.
                    #  cand[0] => '201'
                    #  cand[0][0] => '2'

                    # 리스트를 비운다
                    cand.clear()
                cand.append(k)  # 현재 학생을 리스트에 추가하기

        # 1등 학생 출력 : 학번, 이름, 평균 점수
        for k in cand:
            print(f'{k} : {students[k]["name"]}, {students[k]["avg"]}')

    elif select == '4':
        """
        4. 모든 학생 보기
        현재 등록되어있는 모든 학생들의 모든 정보를 출력하세요.
        """
        for k, v in students:
            print(f'{k}'
                  f' / {students[num]["name"]}'
                  f' / 평균 {students[num]["avg"]}점'
                  f' / 학점 {students[num]["grade"]}'
                  f' / {students[num]["contact"]}')
    else:
        print('잘못된 입력')

