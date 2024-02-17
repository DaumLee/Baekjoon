import sys
from math import sqrt
input = sys.stdin.readline


def is_prime(num):
    # 소수 판별
    for i in range(2, int(sqrt(num))+1):
        # 나누어 떨어지는 경우 소수가 아님
        if not num % i:
            return False
    return True


def solve(n, st):
    global N, ans, next

    if n == N:
        ans.append(int(st))
        return

    # 홀수를 뒤에 붙임
    for i in next:
        # 소수면 뒤에 붙여서 자릿수를 늘림
        if is_prime(int(st + str(i))):
            solve(n+1, st+str(i))


N = int(input())
# 최고차항은 소수로 시작
first = [2, 3, 5, 7]
# 이후에는 5를 제외한 홀수만 들어갈 수 있음
next = [1, 3, 7, 9]
ans = []
for i in first:
    solve(1, str(i))

print(*ans, sep='\n')