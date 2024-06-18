for t in range(int(input())):
    n = input()
    v = ['a', 'e', 'i', 'o', 'u']
    if n[-1] in v:
        s = 'a queen'
    elif n[-1] == 'y':
        s = 'nobody'
    else:
        s = 'a king'
    print(f'Case #{t+1}: {n} is ruled by {s}.')