def mul(a, b):
    if b == 1:
        return a % C
    if b % 2:
        return (mul(a, b//2) ** 2 * a) % C
    else:
        return mul(a, b//2) ** 2 % C


A, B, C = map(int, input().split())
print(mul(A, B))