import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0
for i in coin[::-1]:
    if K >= i:
        cnt += K // i
        K -= i*(K//i)
    if K == 0:
        break

print(cnt)