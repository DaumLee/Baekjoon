from itertools import combinations

L, C = map(int, input().split())
S = sorted(list(input().split()))
a = {'a', 'e', 'i', 'o', 'u'}
ans = []
for c in combinations(S, L):
    if a.intersection(c) and L-len(a.intersection(c)) >= 2:
        ans.append(''.join(list(c)))
print(*sorted(ans), sep='\n')