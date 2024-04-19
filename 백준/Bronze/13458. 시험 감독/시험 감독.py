N = int(input())
lst = list(map(int, input().split()))
mx1, mx2 = map(int, input().split())
ans = 0
for people in lst:
    ans += 1
    trash = people-mx1
    if trash <= 0:
        continue
    else:
        ans += trash//mx2
        if trash%mx2:
            ans += 1
print(ans)