from itertools import combinations


# num과 ans를 검사하는데 idx는 스트라이크 인덱스, b는 볼의 개수
def check(num, ans, idx, b):
    cnt = 0
    for i in range(3):
        # 스트라이크 위치가 아닌 부분만 체크
        if i != idx:
            # 볼이면 +1
            if ans[i] in num and ans[i] != num[i]:
                cnt += 1
            # 스트라이크 위치가 아닌데 스트라이크면
            elif ans[i] == num[i]:
                return False

    # 볼 개수가 검사한 값과 같으면 True
    if cnt != b:
        return False
    return True

# 전체 정답 후보 저장
ans = set()
for i in range(123, 988):
    num = str(i)
    if '0' in num:
        continue
    # 값이 다르면 저장
    elif num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:
        ans.add(num)

lst = []
for _ in range(int(input())):
    num, s, b = input().split()
    lst.append((int(s), num, int(b)))
lst.sort(key=lambda x: (-(x[0]+x[2]), -x[0]))

# 3스트라이크가 있으면
if lst[0][0] == 3:
    print(1)
else:
    # item = [스트라이크 개수(int), 숫자(str), 볼 개수(int)]
    for item in lst:
        tmp = set()
        # 2 스트라이크면
        if item[0] == 2:
            # 인덱스 중 2개를 골라서
            for i in combinations([0, 1, 2], 2):
                nidx = 3-(i[0]+i[1])
                # 정답을 순회하면서
                for a in ans:
                    # 주어진 값과 2 스트라이크면
                    if a[i[0]] == item[1][i[0]] and a[i[1]] == item[1][i[1]] and a[nidx] != item[1][nidx]:
                        tmp.add(a)
            # 교집합 정리
            ans = ans.intersection(tmp)
        # 1 스트라이크면
        elif item[0] == 1:
            tmp = set()
            # 3개 중 하나만 정답
            for i in range(3):
                for a in ans:
                    # 주어진 값과 1 스트라이크면
                    if a[i] == item[1][i]:
                        if check(item[1], a, i, item[2]):
                            tmp.add(a)
            # 교집합 정리
            ans = ans.intersection(tmp)
        else:
            tmp = set()
            for a in ans:
                if check(item[1], a, 4, item[2]):
                    tmp.add(a)
            # 교집합 정리
            ans = ans.intersection(tmp)
    print(len(ans))