"""

    사용자에게 주민번호를 입력 받아 생일,나이,성별을 출력하세요.
    
    YYMMDD-GXXXXXX
    
    G :
        1 => 1900년대 남성
        2 => 1900년대 여성
        3 => 2000년대 남성
        4 => 2000년대 여성
    
"""
user_id = input('주민번호 : ')
year = int(user_id[:2])
month = user_id[2:4]
date = user_id[4:6]
gender = ''

if user_id[7] == '1':
    year += 1900
    gender = '남성'
elif user_id[7] == '2':
    year += 1900
    gender = '여성'
elif user_id[7] == '3':
    year += 2000
    gender = '남성'
elif user_id[7] == '4':
    year += 2000
    gender = '여성'


# 방법1. 2020 고정값으로 나이 구하기
print(f'{year}년 {month}월 {date}일, {2020-year}세, {gender}')


# 방법2. 올해가 몇년인지 구하고 나이 구하기
import datetime
nw = datetime.datetime.now()
print(f'{year}년 {month}월 {date}일, {nw.year-year}세, {gender}')







