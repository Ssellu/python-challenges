"""

    사용자에게 년,월,일을 입력 받고
    1월 1일부터 해당 날짜까지 며칠이 소요되는 지 출력하세요.
    윤년을 포함하세요.
        => 윤년 : year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
    2020 1 30  ==> 29일 소요!
    2020 12 31 ==> 365일 소요! (윤년)

"""

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start = input('YYYYMMDD : ')

total = 0
s_year = int(start[:4])
s_month = int(start[4:6])
s_date = int(start[6:])

if s_year % 400 == 0 or (s_year % 100 != 0 and s_year % 4 == 0):
    dates[1] = 29

for m in range(s_month - 1):
    total += dates[m]
total += s_date - 1

print(f'{s_year}/1/1 ~ {s_year}/{s_month}/{s_date} : {total}')

"""
    시작일 : YYYYMMDD 형태의 문자열로 입력 받습니다.
    목표일 : YYYYMMDD 형태의 문자열로 입력 받습니다.
    시작일로부터 목표일까지 며칠이 소요되는 지 출력하세요.
    목표일은 시작일보다 미래입니다.
"""

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = []

start = input('Date to start (YYYYMMDD) : ')
goal = input('Date to end (YYYYMMDD) : ')

s_total = 0
s_year = int(start[:4])
s_month = int(start[4:6]) - 1
s_date = int(start[6:])

g_total = 0
g_year = int(goal[:4])
g_month = int(goal[4:6]) - 1
g_date = int(goal[6:])

print(f'{s_year}/{s_month+1}/{s_date} ~ {g_year}/{g_month+1}/{g_date}')

for y in range(s_year, g_year + 1):
    tmp = dates.copy()
    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        tmp[1] += 1
    total.append(tmp)

d_day = 0
m = s_month
n = 0
while n < len(total):
    l = g_month if n == len(total)-1 else len(total[n])
    while m < l:
        d_day += total[n][m]
        total[n][m] = 0
        m += 1
    m = 0
    n += 1

d_day += (-s_date) + g_date
print(f'D\'day : {d_day}')
for n in total:
    print(n)

"""
    참고) 파이썬의 디데이 구하는 진짜 방법
    import datetime

    start = datetime.date(2020, 1, 23)
    end = datetime.date(2020, 11, 23)
    delta = end - start
    print(delta.days)
"""

