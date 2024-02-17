N = int(input())
lst = []
# e, s 순으로 리스트에 넣음(정렬을 위함)
for _ in range(N):
    s, e = map(int, input().split())
    lst.append((e, s))

# 종료 시간이 이른 순 정렬
lst.sort()
# 회의 진행 카운트
cnt = 0
# 회의가 끝나는 시간
end = 0
for e, s in lst:
    # 마지막 회의가 끝난 이후부터 시작 가능
    if s >= end:
        # 끝나는 시간 갱신
        end = e
        cnt += 1

print(cnt)