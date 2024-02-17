N = int(input())
lst = list(map(int, input().split()))
stk = [[lst[0], 0]]
idx = 1
ans = [0] * N
for i in range(1, N):
    while stk and idx < N:
        # 스택에 넣을 값이 더 작으면(통신 가능)
        if lst[i] < stk[-1][0]:
            ans[i] = stk[-1][1]+1
            stk.append([lst[i], i])
            idx += 1
            break
        # 스택에 넣을 값이 더 크면 하나 뺌
        else:
            stk.pop()
    # 스택이 비었으면
    else:
        stk.append([lst[i], i])
        idx += 1
print(*ans)