N = int(input())
lst = [int(input()) for _ in range(N)]

# 키, 개수 순으로 삽입
stk = []
ans = 0
for i in lst:
    # 앞서 있는 사람이 나보다 작다면 쌍이 됨
    while stk and stk[-1][0] < i:
        ans += stk.pop()[1]

    # 스택이 비었으면 append(1개)
    if not stk:
        stk.append((i, 1))
    # 스택에 값이 있다면
    else:
        # 마지막 값과 비교해서 키가 같으면 서로 볼 수 있음
        if stk[-1][0] == i:
            cnt = stk.pop()[1]
            ans += cnt
            if stk:
                ans += 1
            # 똑같은 쌍이 cnt + 1 개 만큼 존재
            stk.append((i, cnt+1))
        else:
            stk.append((i, 1))
            ans += 1

print(ans)