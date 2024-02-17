T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    _ = [input() for _ in range(M)]
    print(N-1)