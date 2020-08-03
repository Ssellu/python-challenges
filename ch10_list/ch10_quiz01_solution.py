"""

    리스트 a 에 대하여 다음 작업을 수행하세요.
        1) 사용자에게 정수를 6번 입력 받아 차례대로 a에 저장
        2) 사용자에게 인덱스를 입력 받아 해당 인덱스에 위치한 원소 출력
        3) 사용자에게 원소를 입력 받아 해당 리스트에 있는지 출력
        4) a의 원소 중 짝수만 출력 + 그의 개수 출력
        5) 최댓값과 최솟값 출력
        6) 오름차순 정렬하여 결과 출력
"""

a = [0, 0, 0, 0, 0, 0]

# 1) 사용자에게 정수를 6번 입력 받아 차례대로 a에 저장
i = 0
for i in range(len(a)):
    a[i] = int(input(f'a[{i}] : '))

# 2) 사용자에게 인덱스를 입력 받아 해당 인덱스에 위치한 원소 출력
i = int(input('인덱스:'))
if i >= len(a) or i < -len(a):
    print('유효하지 않은 인덱스')
else:
    print(f'a[{i}] : {a[i]}')

# 3) 사용자에게 원소를 입력 받아 해당 리스트에 있는지 출력
e = int(input('검색할 원소:'))
if e in a:
    print(f'{e}(은)는 있습니다.')
else:
    print(f'{e}(은)는 없습니다.')

# 4) a의 원소 중 짝수만 출력 + 그의 개수 출력
print('짝수만 출력하기 : ', end='')
cnt = 0
for e in a:
    if e % 2 == 0:
        print(e, end=", ")
        cnt += 1
print(f'총 {cnt}개')

# 5) 최댓값과 최솟값 출력
mx = a[0]
mn = a[0]
for e in a:
    if mx < e:
        mx = e
    if mn > e:
        mn = e
print(f'최댓값 : {mx}, 최솟값 : {mn}')

# 6) 오름차순 정렬하여 결과 출력
# 방법1 - sort() 사용
# a.sort()
# print(f'오름차순 결과 : {a}')

# 방법2 - 직접 정렬 (선택정렬알고리즘)
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(f'오름차순 결과 : {a}')
