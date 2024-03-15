def scoring(si, sj, d1, d2):
    sm1 = sm2 = sm3 = sm4 = 0

    y = sj+1
    for i in range(si+d1):
        # 시작점을 넘어선 순간부터는 1씩 열이 깎임
        if i >= si:
            y -= 1
        for j in range(y):
            sm1 += arr[i][j]

    y = sj+1
    for i in range(si+d2+1):
        # 시작점을 넘어선 순간부터는 1씩 열이 깎임
        if i > si:
            y += 1
        for j in range(y, N):
            sm2 += arr[i][j]

    y = sj-d1-1
    for i in range(si+d1, N):
        # 끝점에 가기 전까지는 도착 열이 오른쪽으로 감
        if i <= si+d1+d2:
            y += 1
        for j in range(y):
            sm3 += arr[i][j]

    y = sj+d2+1
    for i in range(si+d2+1, N):
        # 끝점에 가기 전까지는 시작 열이 왼쪽으로 감
        if i <= si+d1+d2+1:
            y -= 1
        for j in range(y, N):
            sm4 += arr[i][j]

    sm5 = pop - (sm1 + sm2 + sm3 + sm4)
    return max(sm1, sm2, sm3, sm4, sm5) - min(sm1, sm2, sm3, sm4, sm5)


def divide(si, sj):
    global ans
    # 여기서 i와 j는 d1, d2를 뜻함
    for i in range(1, N):
        for j in range(1, N):
            if si+j < N and 0 <= sj-i and si+i+j < N and sj+j < N:
                score = scoring(si, sj, i, j)
                ans = min(ans, score)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 전체 인구
pop = 0
for i in range(N):
    pop += sum(arr[i])
# 정답은 일단 최대 인구를 넣음
ans = pop
for i in range(N-2):
    for j in range(1, N-1):
        divide(i, j)

print(ans)