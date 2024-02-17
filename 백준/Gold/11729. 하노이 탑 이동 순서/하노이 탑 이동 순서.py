# 옮길 원반 개수, 시작 / 중간 / 목적지 번호
def hanoi(n, s, t, e):
    global cnt
    # 마지막 하나는 바로 옮김
    if n == 1:
        ans.append((s, e))
        cnt += 1
        return

    # 두개 이상 남으면 위에서부터 n-1개를 중간 막대에 보내고(과정 생략하고)
    hanoi(n-1, s, e, t)
    # 판에서 제일 큰 원반을 목적지에 옮김(해당 원반 이동 종료)
    hanoi(1, s, t, e)
    # 이제 남은 n-1개를 t에서부터 s를 거쳐서 e까지 보내면 하노이의 탑 종료
    hanoi(n-1, t, s, e)


N = int(input())
cnt = 0
ans = []
hanoi(N, 1, 2, 3)
print(cnt)
for i in range(cnt):
    print(*ans[i])