N = int(input())
graph = dict()

for n in range(N):
    p, s1, s2 = input().split()
    graph[p] = [s1, s2]


def preorder(p, trav):

    if p != '.':
        # 부모 순회
        trav.append(p)
        # 왼쪽 순회
        preorder(graph[p][0], trav)
        # 오른쪽 순회
        preorder(graph[p][1], trav)

    return (''.join(trav))


def inorder(p, trav):

    if p != '.':
        # 왼쪽 순회
        inorder(graph[p][0], trav)
        # 부모 순회
        trav.append(p)
        # 오른쪽 순회
        inorder(graph[p][1], trav)

    return (''.join(trav))


def postorder(p, trav):

    if p != '.':
        # 왼쪽 순회
        postorder(graph[p][0], trav)
        # 오른쪽 순회
        postorder(graph[p][1], trav)
        # 부모 순회
        trav.append(p)

    return (''.join(trav))


print(preorder('A', []))
print(inorder('A', []))
print(postorder('A', []))