"""

 다음은 1부터 시작하는 피보나치 수열의 n번째 수를 구하는 재귀함수 입니다.
 n이 10일 때 총 몇 회의 fibonacci() 가 수행되는 지 적으세요.
 (+그 과정도 서술해주시면 좋습니다.)

"""


def fibonacci(n: int) -> int:
    if n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(3))  # 2
print(fibonacci(4))  # 3
print(fibonacci(5))  # 5
