arr = []

for i in range(10):
    a = int(input())
    b = a % 42
    if i == 0:
        arr.append(b)
    for j in range(len(arr)):
        if b not in arr:
            arr.append(b)
    
print(len(arr))