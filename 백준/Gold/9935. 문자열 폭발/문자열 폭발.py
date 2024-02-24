import sys
from collections import deque
from itertools import islice
input = sys.stdin.readline

st = list(input().rstrip())
bomb = list(input().rstrip())
N = len(bomb)
q = deque()

for i in range(len(st)):
    # i번째 문자열을 앞에 넣음
    q.appendleft(st[i])
    # 문자열을 추가해서 앞의 N개가 bomb을 뒤집은 것과 같다면(큐에 뒤집어서 넣기 때문)
    if list(islice(q, 0, N)) == bomb[::-1]:
        for _ in range(N):
            q.popleft()

if q:
    print(''.join(reversed(q)))
else:
    print("FRULA")