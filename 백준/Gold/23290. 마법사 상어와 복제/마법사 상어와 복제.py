def fish_move():
    for i in range(4):
        for j in range(4):
            if arr[i][j]:
                for nxt_d in arr[i][j]:
                    d = nxt_d
                    for _ in range(8):
                        di, dj = delta[d]
                        ni, nj = i+di, j+dj
                        # 범위 내에서 냄새가 없는 칸 이동 가능
                        if 0 <= ni < 4 and 0 <= nj < 4 and not smell[ni][nj] and (ni, nj) != (si, sj):
                            nxt_arr[ni][nj].append(d)
                            break
                        else:
                            d = (d-1)%8
                    else:
                        nxt_arr[i][j].append(d)


def shark_move(n, route):
    global mx, nxt_i, nxt_j, smells

    # 최대 케이스를 찾았다면 사전 순 상어 루트 탐색 중단, 조건 실수 (2시 42분)
    # if mx == 3:
    #     return
    if n == 3:
        score, ni, nj, eats = counting(si, sj, route)
        # 최댓값을 갱신했을 때만
        if score > mx:
            mx = score
            nxt_i = ni
            nxt_j = nj
            smells = eats
        return

    for sd in range(1, 5):
        shark_move(n+1, route+[sd])


def counting(si, sj, route):
    ci, cj = si, sj
    cnt = 0
    eat = []
    # 시작 칸에 물고기가 있다면? (2시 40분)
    # if nxt_arr[ci][cj]:
    #     print(1)
    #     cnt += len(nxt_arr[ci][cj])
    #     eat.append((ci, cj))
    # 방향으로 진행 가능 여부 체크
    for sd in route:
        di, dj = s_delta[sd]
        ni, nj = ci+di, cj+dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 이동 방향에 물고기가 있으면
            if nxt_arr[ni][nj] and (ni, nj) not in eat:
                cnt += len(nxt_arr[ni][nj])
                eat.append((ni, nj))
            # 이동을 마치고 위치 갱신
            ci, cj = ni, nj
        # 이동할 수 없는 칸
        else:
            return -1, si, sj, []
    # 먹은 물고기 수와 마지막 위치, 먹은 물고기 좌표를 리턴
    return cnt, ci, cj, eat


M, S = map(int, input().split())
# 물고기 이동
# delta = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
delta = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
# 상어의 방향
s_delta = ((0, 0), (-1, 0), (0, -1), (1, 0), (0, 1))
# 방향 저장
arr = [[list() for j in range(4)] for i in range(4)]
# 냄새 저장
smell = [[0 for j in range(4)] for i in range(4)]
for num in range(1, M+1):
    fi, fy, d = map(int, input().split())
    arr[fi-1][fy-1].append(d-1)
si, sj = map(int, input().split())
si -= 1
sj -= 1
for time in range(1, S+1):
    nxt_arr = [[list() for j in range(4)] for i in range(4)]
    fish_move()
    # 먹을 수 있는 물고기의 최댓값
    mx = -1
    # 다음 상어의 위치
    nxt_i = 0
    nxt_j = 0
    # 냄새를 뿌릴 위치
    smells = []
    shark_move(0, [])
    # 상어 위치 갱신
    si, sj = nxt_i, nxt_j
    # 냄새를 먼저 제거하고
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 2턴 지속되는 냄새를 뿌림
    for smi, smj in smells:
        smell[smi][smj] = 2
        # 물고기를 지움
        nxt_arr[smi][smj] = []
    # 복제 완료
    for i in range(4):
        for j in range(4):
            if arr[i][j]:
                nxt_arr[i][j].extend(arr[i][j])
    # 보드 교체
    arr = nxt_arr

ans = 0
for i in range(4):
    for j in range(4):
        if arr[i][j]:
            ans += len(arr[i][j])
print(ans)