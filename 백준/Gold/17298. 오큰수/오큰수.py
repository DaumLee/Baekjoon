N = int(input())
lst = list(map(int, input().split()))
stk = []
idx = 0
ans = [-1] * N
for i in range(N):
    while stk:
        # 이전에 나왔던 숫자보다 크면
        if lst[i] > stk[-1][0]:
            s = stk.pop()
            # 지금 숫자를 정답으로 출력
            ans[s[1]] = lst[i]
        else:
            # 나보다 작은 수가 없으면 스택에 넣고 다음 인자와 비교함
            stk.append([lst[i], i])
            idx += 1
            break
    # 스택이 비었으면 일단 스택에 넣고 다음 인자로 넘어감
    else:
        stk.append([lst[i], i])
        idx += 1

print(*ans)