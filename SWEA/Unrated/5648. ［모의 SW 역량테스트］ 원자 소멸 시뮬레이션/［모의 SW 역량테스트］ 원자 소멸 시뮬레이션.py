class Atom:
    def __init__(self, i, j, d, k):
        self.i = i
        self.j = j
        self.d = d
        self.k = k

    def __str__(self):
        return f'({self.i}, {self.j}), 방향 : {self.d}, 에너지 :  {self.k}'


def find_couple():
    mn = -1
    crashed = set()
    for a in range(1, N+1):
        if not status[a]: continue
        a_val = atoms[a]
        ai, aj, ad = a_val.i, a_val.j, a_val.d
        adi, adj = delta[ad]
        for b in range(a+1, N+1):
            if not status[b]: continue
            b_val = atoms[b]
            bi, bj, bd = b_val.i, b_val.j, b_val.d
            bdi, bdj = delta[bd]
            # 한 칸만 이동했을 때 거리가 줄어들면 만날 가능성 존재
            if abs((ai+adi)-(bi+bdi))+abs((aj+adj)-(bj+bdj)) <= abs(ai-bi)+abs(aj-bj):
                # 서로 반대 방향인 경우
                if ad^1 == bd:
                    # 상하 이동이면
                    if ad <= 1 and aj == bj:
                        dist = (abs(ai-bi))/2
                    # 좌우 이동이면
                    elif ad >= 2 and ai == bi:
                        dist = (abs(aj-bj))/2
                    # 만나지 못하는 경우
                    else:
                        continue
                    # 최소 거리만 부딪힐 수 있음
                    if mn == -1 or dist < mn:
                        mn = dist
                        crashed = {a, b}
                    elif dist == mn:
                        crashed.add(a)
                        crashed.add(b)
                # ㄱ자 이동인 경우
                elif ad != bd and abs(ai-bi) == abs(aj-bj) and abs(ai+adi-bi-bdi) == abs(aj+adj-bj-bdj):
                    dist = abs(ai-bi)
                    # 최소 거리만 부딪힐 수 있음
                    if mn == -1 or dist < mn:
                        mn = dist
                        crashed = {a, b}
                    # 같은 시간대에 부딪히는 경우
                    elif dist == mn:
                        crashed.add(a)
                        crashed.add(b)
    return crashed


def crash(lst):
    global ans
    for num in lst:
        atom = atoms[num]
        ans += atom.k
        status[num] = False


delta = ((1, 0), (-1, 0), (0, -1), (0, 1))
for tc in range(1, int(input())+1):
    N = int(input())
    atoms = dict()
    # 살아있는지 확인
    status = {i: True for i in range(1, N+1)}
    for num in range(1, N+1):
        j, i, d, k = map(int, input().split())
        atoms[num] = Atom(i, j, d, k)
    ans = 0
    while True:
        # 충돌하는 짝 찾기
        clst = find_couple()
        if not clst:
            break
        # 충돌 진행
        crash(clst)
    print(f'#{tc} {ans}')