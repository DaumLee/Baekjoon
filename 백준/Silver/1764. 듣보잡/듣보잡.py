N, M = map(int, input().split())

# 듣
unheard = set()
for i in range(N):
    unheard.add(input())
    
# 보
unseen = set()
for i in range(M):
    unseen.add(input())

# 듣보
unknown = unheard.intersection(unseen)
print(len(unknown), *sorted(unknown), sep='\n')