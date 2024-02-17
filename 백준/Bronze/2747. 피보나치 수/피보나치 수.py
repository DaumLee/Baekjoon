def fibo(n):
    if n >= N+1:
        return
    lst.append(lst[n-1] + lst[n-2])
    fibo(n+1)


N = int(input())
lst = [0, 1, 1]
fibo(3)
print(lst[N])