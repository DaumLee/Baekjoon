# 난쟁이 키
lst = [int(input()) for _ in range(9)]
# 전체 합
sm = sum(lst)

for i in range(9):
    # 외부인 검문
    find = sm - 100 - lst[i]
    # 검문 성공 시
    if find in lst[i+1:]:
        # 송환
        lst.pop(lst.index(find))
        lst.pop(i)
        break

lst.sort()
for i in range(len(lst)):
    print(lst[i])