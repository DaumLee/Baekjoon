def switch(x):
    if lst[x]:
        lst[x] = 0
    else:
        lst[x] = 1


def male(n):
    # 리스트 전체 순회
    for i in range(n-1, N):
        # n의 배수이면 상태 변경
        if not (i+1) % n:
            switch(i)


def female(n):
    # 3번 스위치면 lst[2], 번호와 인덱스 맞추기
    n -= 1
    for i in range(1, N//2+1):
        # 왼쪽, 오른쪽 확인
        l, r = n-i, n+i
        # 인덱스 범위를 벗어나면 종료
        if l < 0 or r >= N:
            for j in range(l+1, r):
                switch(j)
            return
        # 대칭이 아니면 이전까지만 바꿈
        if lst[l] != lst[r]:
            for j in range(l+1, r):
                switch(j)
            return


N = int(input())
lst = list(map(int, input().split()))

for i in range(int(input())):
    s, n = map(int, input().split())
    if s == 1:
        male(n)
    else:
        female(n)

if N < 21:
    print(*lst)
elif N < 41:
    print(*lst[:20])
    print(*lst[20:])
elif N < 61:
    print(*lst[:20])
    print(*lst[20:40])
    print(*lst[40:])
elif N < 81:
    print(*lst[:20])
    print(*lst[20:40])
    print(*lst[40:60])
    print(*lst[60:])
else:
    print(*lst[:20])
    print(*lst[20:40])
    print(*lst[40:60])
    print(*lst[60:80])
    print(*lst[80:])