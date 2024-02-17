N = int(input())
stk = []
for _ in range(N):
    item = int(input())
    if stk:
        if item >= stk[-1]:
            for i in range(len(stk)-1, -1, -1):
                if stk[i] <= item:
                    stk.pop()
                else:
                    break
            stk.append(item)
        else:
            stk.append(item)
    else:
        stk.append(item)

print(len(stk))