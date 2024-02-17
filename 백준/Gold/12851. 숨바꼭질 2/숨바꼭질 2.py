from collections import deque


def bfs(s, e):
    q = deque()
    v = [0] * (int(10e4)+1)
    q.append(s)
    v[s] = 0
    cnt = 0
    ret = 10e4

    while q:
        c = q.popleft()
        if v[c] > ret:
            break
        if c == e:
            ret = v[c]
            cnt += 1
            continue
        for n in (c-1, c+1, c*2):
            if 0 <= n <= 10e4 and (not v[n] or v[c]+1 == v[n]):
                q.append(n)
                v[n] = v[c] + 1
    return v[e], cnt


N, K = map(int, input().split())

if N == K:
    print(0)
    print(1)
else:
    ans = bfs(N, K)
    print(ans[0])
    print(ans[1])