"""
    2. 1 ~ 1000 중 11과 13의 공배수를 출력하고 그의 개수를 출력하세요. (for 문)

"""
cnt = 0
# 방법1
# for n in range(1, 1001):
#     if n % 11 == 0 and n % 13 == 0:
#         print(n)
#         cnt += 1
# print(f'총 {cnt}개')

# 방법2
for n in range(143, 1001, 143):
    print(n)
    cnt += 1
print(f'총 {cnt}개')
