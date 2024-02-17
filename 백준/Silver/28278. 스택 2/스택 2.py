import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    l = sys.stdin.readline().split()

    if l[0] == "1":
        if len(stack) == 0:
            stack = [int(l[1])]
        else:
            stack.append(int(l[1]))
    elif l[0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif l[0] == "3":
        print(len(stack))
    elif l[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
