N = int(input())
# 수열
lst = [int(input()) for _ in range(N)]
# 스택(empty 케이스를 제거하기 위해 0을 맨 앞에 삽입)
stk = [0]
# 수열의 idx
idx = 0
# 출력할 정답
ans = []

for i in range(1, N+1):
    # 스택 마지막 값이 수열과 같으면 pop
    while stk[-1] == lst[idx]:
        stk.pop()
        ans.append('-')
        idx += 1
    # 입력값이 수열보다 작으면 push
    if i < lst[idx]:
        stk.append(i)
        ans.append('+')
    # 입력값이 수열과 같으면 push 후 pop
    elif i == lst[idx]:
        ans.append('+')
        ans.append('-')
        idx += 1
    # 입력값이 수열보다 크면 이후로는 계속 pop
    else:
        break

# 모든 수를 pop하면서 수열과 검증
while stk and idx < N:
    if stk[-1] == lst[idx]:
        ans.append('-')
        stk.pop()
        idx += 1
    else:
        ans = ['NO']
        break

for i in ans:
    print(i)