lst = list(input())
# 임시 스택
stk = []
# 정답 저장
ans = []
# 하나씩 순회
for item in lst:
    # 알파벳은 그대로 넣고
    if 65 <= ord(item) <= 90:
        ans.append(item)
    # 괄호가 열리면 스택으로
    elif item == '(':
        stk.append(item)
    # 우선순위 연산이 들어오면 이전에 들어온 연산을 스택에서 제거하고 위에 담음
    elif item == '*' or item == '/':
        while stk:
            if stk[-1] == '*' or stk[-1] == '/':
                ans.append(stk.pop())
            else:
                break
        stk.append(item)
    # 후순위 연산이 들어오면
    elif item == '+' or item == '-':
        while stk:
            if stk[-1] != '(':
                ans.append(stk.pop())
            else:
                break
        stk.append(item)
    # 괄호가 닫히면 전부 제거
    elif item == ')':
        while stk:
            if stk[-1] != '(':
                ans.append(stk.pop())
            else:
                break
        # 여는 괄호는 후위 표기식에서 사용하지 않음
        stk.pop()

# 남은 거 다 갖다 붙이면 끝
while stk:
    ans.append(stk.pop())
print(*ans, sep='')