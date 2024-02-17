N = int(input())
ans = 0
for _ in range(N):
    lst = input()
    stk = [lst[0]]
    for i in range(1, len(lst)):
        if not stk:
            stk.append(lst[i])
        else:
            if stk[-1] != lst[i]:
                stk.append(lst[i])
            else:
                stk.pop()
    if not stk:
        ans += 1
print(ans)