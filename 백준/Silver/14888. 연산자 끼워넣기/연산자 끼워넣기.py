def calculate(exp):
    stk = [exp[0]]
    for i in exp[1:]:
        # 숫자가 들어오면 두개 pop해서 연산
        if i not in op:
            o = stk.pop()
            pre = stk.pop()
            if o == '+':
                stk.append(pre + int(i))
            elif o == '-':
                stk.append(pre - int(i))
            elif o == '*':
                stk.append(pre * int(i))
            else:
                if pre < 0:
                    stk.append(((pre*(-1)) // int(i))*-1)
                else:
                    stk.append(pre // int(i))
        # 연산자가 들어오면 스택에 넣기만 함
        else:
            stk.append(i)
    # 최종 결과 값을 정답 배열에 추가
    ans.append(stk[0])


def solve(n, i, exp):
    if n == length-1:
        calculate(exp)
        return

    if i+1 > N-1:
        return

    for o in range(4):
        if oper[o]:
            oper[o] -= 1
            solve(n+2, i+1, exp+[op[o]]+[lst[i+1]])
            oper[o] += 1


N = int(input())
lst = list(map(int, input().split()))
# 연산자 개수
oper = list(map(int, input().split()))
op = ['+', '-', '*', '/']
# 총 수식 길이
length = sum(oper) + N
# 정답 모두 저장
ans = []
solve(0, 0, [lst[0]])

print(max(ans))
print(min(ans))