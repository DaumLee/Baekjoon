N = int(input())
sm = 0

for i in range(1, N):
    temp = i
    for j in range(i+1, N):
        if temp + j < N:
            temp += j
        elif temp + j == N:
            sm += 1
            break
        elif temp + j > N:
            break

print(sm+1)