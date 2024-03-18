def scoring(archer):
    board = [lst[:] for lst in arr]
    score = 0
    while board:
        enemy = []
        cnt = 0
        for i in range(len(board)):
            for j in range(M):
                if board[i][j]:
                    enemy.append((i, j))
                    cnt += 1
        if not cnt:
            return score
        atk = []
        for k in archer:
            cand = []
            r = D
            for ei, ej in enemy:
                if abs(len(board)-ei)+abs(k-ej) < r:
                    r = abs(len(board)-ei)+abs(k-ej)
                    cand = [(ei, ej)]
                elif abs(len(board)-ei)+abs(k-ej) == r:
                    cand.append((ei, ej))
            # 공격할 수 있으면
            if cand:
                ai = aj = M
                for ci, cj in cand:
                    if cj < aj:
                        ai, aj = ci, cj
                atk.append((ai, aj))
        # 공격 가능한 경우
        if atk:
            for ai, aj in atk:
                if board[ai][aj]:
                    board[ai][aj] = 0
                    score += 1
        board.pop()
    return score

def solve(n, idx, arc):
    global ans
    if n == 3:
        ans = max(ans, scoring(arc))
        return

    for i in range(idx+1, M):
        solve(n+1, i, arc+[i])

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
solve(0, -1, [])

print(ans)