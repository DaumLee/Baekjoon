ans = []
while True:
    try:
        N, S = map(int, input().split())
        ans.append(S//(N+1))
    except:
        for x in ans:
            print(x)
        break