T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    cnt = 0
    j = 1
    for _ in range(H*N+1):
        for i in range(1, H+1):
            cnt += 1
            if cnt == N:
                if j // 10 > 0:
                    print(f'{i}{j}')
                else:
                    print(f'{i}0{j}')
        j += 1