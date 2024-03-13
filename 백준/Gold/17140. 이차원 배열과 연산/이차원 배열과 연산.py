def R(A):
    new_A = []
    # 최대 길이
    mx = 0
    for i in range(len(A)):
        cnts = [0] * 101
        lst = A[i]
        for i in lst:
            cnts[i] += 1
        new_lst = []
        for v in range(1, 101):
            for c in range(1, 101):
                # 0개는 확인하지 않고
                if cnts[c] == 0: continue
                # 최솟값은 크기 순으로 값, 개수를 new_lst에 추가
                if cnts[c] == v:
                    new_lst.append(c)
                    new_lst.append(v)
        mx = max(mx, len(new_lst[:101]))
        new_A.append(new_lst[:101])
    for i in range(len(new_A)):
        if len(new_A[i]) < mx:
            new_A[i] = new_A[i] + [0]*(mx - len(new_A[i]))
    return new_A


def C(A):
    new_A = []
    # 최대 길이
    mx = 0
    for j in range(len(A[0])):
        cnts = [0] * 101
        for i in range(len(A)):
            cnts[A[i][j]] += 1
        new_lst = []
        for v in range(1, 101):
            for c in range(1, 101):
                # 0개는 확인하지 않고
                if cnts[c] == 0: continue
                # 최솟값은 크기 순으로 값, 개수를 new_lst에 추가
                if cnts[c] == v:
                    new_lst.append(c)
                    new_lst.append(v)
        mx = max(mx, len(new_lst[:101]))
        new_A.append(new_lst[:101])
    for i in range(len(new_A)):
        if len(new_A[i]) < mx:
            new_A[i] = new_A[i] + [0]*(mx - len(new_A[i]))

    ret_A = [[0] * len(new_A) for _ in range(len(new_A[0]))]
    for i in range(len(new_A)):
        for j in range(len(new_A[0])):
            ret_A[j][i] = new_A[i][j]
    return ret_A

ei, ej, k = map(int, input().split())
ei -= 1
ej -= 1
A = [list(map(int, input().split())) for _ in range(3)]

time = 0
while True:
    if ei < len(A) and ej < len(A[0]) and A[ei][ej] == k:
        print(time)
        break
    if time > 100:
        print(-1)
        break
    if len(A) >= len(A[0]):
        A = R(A)
    else:
        A = C(A)
    time += 1