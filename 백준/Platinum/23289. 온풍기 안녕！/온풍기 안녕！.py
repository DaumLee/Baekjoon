from collections import deque


# def print1(arr, pre, nxt):
#     for i in range(N):
#         for j in range(M):
#             print(f'{arr[i][j]:>4}', end=' ')
#         print('    ', end=' ')
#         for j in range(M):
#             print(f'{pre[i][j]:>4}', end=' ')
#         print('    ', end=' ')
#         for j in range(M):
#             print(f'{nxt[i][j]:>4}', end=' ')
#         print()


def turn_on(si, sj, sd):
    v = [[0] * M for _ in range(N)]
    if sd == 1:
        q = deque([(si, sj+1)])
    elif sd == 2:
        q = deque([(si, sj-1)])
    elif sd == 3:
        q = deque([(si-1, sj)])
    else:
        q = deque([(si+1, sj)])
    nq = deque()
    for k in range(5, 0, -1):
        for _ in range(len(q)):
            ci, cj = q.popleft()
            arr[ci][cj] += k
            if sd == 1:
                if cj+1 == M:
                    continue
                ni, nj = ci-1, cj+1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 0 in wall[ci][cj] and not 1 in wall[ci-1][cj]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci, cj+1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 1 in wall[ci][cj]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci+1, cj+1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 0 in wall[ci+1][cj] and not 1 in wall[ci+1][cj]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
            elif sd == 2:
                if cj == 0:
                    continue
                ni, nj = ci-1, cj-1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 0 in wall[ci][cj] and not 1 in wall[ci-1][cj-1]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci, cj-1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not (1 in wall[ci][cj - 1]):
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci+1, cj-1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 0 in wall[ci+1][cj] and not 1 in wall[ci+1][cj-1]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
            elif sd == 3:
                if ci == 0:
                    continue
                ni, nj = ci-1, cj-1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 1 in wall[ci][cj-1] and not 0 in wall[ci][cj-1]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci-1, cj
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not (0 in wall[ci][cj]):
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci-1, cj+1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 1 in wall[ci][cj] and not 0 in wall[ci][cj+1]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
            else:
                if ci+1 == N:
                    continue
                ni, nj = ci+1, cj-1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 1 in wall[ci][cj-1] and not 0 in wall[ci+1][cj-1]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci+1, cj
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not (0 in wall[ci+1][cj]):
                        nq.append((ni, nj))
                        v[ni][nj] = 1
                ni, nj = ci+1, cj+1
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                    if not 1 in wall[ci][cj] and not 0 in wall[ci+1][cj+1]:
                        nq.append((ni, nj))
                        v[ni][nj] = 1
        q = nq


N, M, K = map(int, input().split())
# 온도 체크 위치
check = []
# 온풍기 위치
heater = []
arr = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] and lst[j] == 5:
            check.append((i, j))
            lst[j] = 0
        elif lst[j]:
            heater.append((i, j, lst[j]))
            lst[j] = 0
    arr.append(lst)
# 벽
W = int(input())
wall = [[list() for j in range(M)] for i in range(N)]
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    wall[x][y].append(t)
# ((출발 좌표), (목적 좌표)) 순으로 저장
# hor_wall = defaultdict(list)
# ver_wall = defaultdict(list)
# 온도 조절 때 확인할 둘 사이의 벽
# wall = defaultdict(list)
# for _ in range(W):
#     x, y, t = map(int, input().split())
#     x -= 1
#     y -= 1
#     num = x*M + y
#     # 가로 벽
#     if t == 1:
#         nxt = x*M+y+1
#         # 바로 옆
#         hor_wall[num].append(nxt)
#         # 반대로도 불가능
#         hor_wall[nxt].append(num)
#         # 한 칸 위에서도 불가능
#         # if x > 0:
#         #     hor_wall[(x-1)*M+y].append(nxt)
#         #     hor_wall[(x-1)*M+y+1].append(num)
#         # 한 칸 아래서도 불가능
#         # if x < N-1:
#         #     hor_wall[(x+1)*M+y].append(nxt)
#         #     hor_wall[(x+1)*M+y+1].append(num)
#         wall[num].append(nxt)
#         wall[nxt].append(num)
#     else:
#         nxt = (x-1)*M+y
#         # 바로 위
#         ver_wall[num].append(nxt)
#         # 반대로도 불가능
#         ver_wall[nxt].append(num)
#         # 한 칸 왼쪽에서도 불가능
#         if y > 0:
#             ver_wall[num-1].append(nxt)
#             ver_wall[nxt-1].append(num)
#         # 한 칸 오른쪽에서도 불가능
#         if y < M-1:
#             ver_wall[num+1].append(nxt)
#             ver_wall[nxt+1].append(num)
#         wall[num].append(nxt)
#         wall[nxt].append(num)
# 시작
time = 0
while time < 100:
    # 온풍기 작동
    for si, sj, d in heater:
        # k = 5
        # if d == 1:
        #     v = [[0] * M for _ in range(N)]
        #     for j in range(sj + 1, M):
        #         if k == 0: break
        #         # 일단 다 뿌리고
        #         for i in range(max(0, si - (5 - k)), min(N, si + 1 + (5 - k))):
        #             # 바람이 못 부는 칸은 건너 뜀
        #             if j != sj + 1 and not v[i][j]: continue
        #             # 다음 진행이 남아 있다면
        #             if k > 1:
        #                 # 다음에 못 두는 칸 찾기
        #                 nxt = []
        #                 # 지금 위치에 관계된 벽이 있다면
        #                 if i * M + j in hor_wall:
        #                     nxt = hor_wall[i * M + j]
        #                 ni = i
        #                 nj = j + 1
        #                 # 다음에 둘 수 있는 칸이라면
        #                 if ni * M + nj not in nxt: v[ni][nj] = 1
        #             arr[i][j] += k
        #         k -= 1
        # elif d == 2:
        #     v = [[0] * M for _ in range(N)]
        #     for j in range(sj - 1, -1, -1):
        #         if k == 0: break
        #         for i in range(max(0, si - (5 - k)), min(N, si + 1 + (5 - k))):
        #             # 일단 다 뿌리고
        #             for i in range(max(0, si - (5 - k)), min(N, si + 1 + (5 - k))):
        #                 # 바람이 못 부는 칸은 건너 뜀
        #                 if j != sj - 1 and not v[i][j]: continue
        #                 # 다음 진행이 남아 있다면
        #                 if k > 1:
        #                     # 다음에 못 두는 칸 찾기
        #                     nxt = []
        #                     # 지금 위치에 관계된 벽이 있다면
        #                     if i * M + j in hor_wall:
        #                         nxt = hor_wall[i * M + j]
        #                     # 다음 칸을 순회하면서
        #                     ni = i
        #                     nj = j + 1
        #                     # 다음에 둘 수 있는 칸이라면
        #                     if ni * M + nj not in nxt: v[ni][nj] = 1
        #             arr[i][j] += k
        #         k -= 1
        # elif d == 3:
        #     v = [[0] * M for _ in range(N)]
        #     for i in range(si - 1, -1, -1):
        #         if k == 0: break
        #         for j in range(max(0, sj - (5 - k)), min(M, sj + 1 + (5 - k))):
        #             # 바람이 못 부는 칸은 건너 뜀
        #             if i != si - 1 and not v[i][j]: continue
        #             # 다음 진행이 남아 있다면
        #             if k > 1:
        #                 # 다음에 못 두는 칸 찾기
        #                 nxt = []
        #                 # 지금 위치에 관계된 벽이 있다면
        #                 if i * M + j in ver_wall:
        #                     nxt = ver_wall[i * M + j]
        #                 # 다음 칸을 순회하면서
        #                 for nj in range(max(0, j - 1), min(M, j + 2)):
        #                     ni = i - 1
        #                     # 다음에 둘 수 있는 칸이라면
        #                     if ni * M + nj not in nxt: v[ni][nj] = 1
        #             arr[i][j] += k
        #         k -= 1
        # else:
        #     v = [[0] * M for _ in range(N)]
        #     for i in range(si + 1, N):
        #         if k == 0: break
        #         for j in range(max(0, sj - (5 - k)), min(M, sj + 1 + (5 - k))):
        #             # 바람이 못 부는 칸은 건너 뜀
        #             if i != si + 1 and not v[i][j]: continue
        #             # 다음 진행이 남아 있다면
        #             if k > 1:
        #                 # 다음에 못 두는 칸 찾기
        #                 nxt = []
        #                 # 지금 위치에 관계된 벽이 있다면
        #                 if i * M + j in ver_wall:
        #                     nxt = ver_wall[i * M + j]
        #                 # 다음 칸을 순회하면서
        #                 for nj in range(max(0, j - 1), min(M, j + 2)):
        #                     ni = i + 1
        #                     # 다음에 둘 수 있는 칸이라면
        #                     if ni * M + nj not in nxt: v[ni][nj] = 1
        #             arr[i][j] += k
        #         k -= 1
        turn_on(si, sj, d)

    # 온도 조절
    new_arr = [lst[:] for lst in arr]
    for i in range(N):
        for j in range(M):
            # 오른쪽으로 인접 체크 가능하면
            if j < M-1:
                if abs(arr[i][j]-arr[i][j+1]) >= 4:
                    if 1 not in wall[i][j]:
                        m = max(arr[i][j], arr[i][j+1]) - min(arr[i][j], arr[i][j+1])
                        if arr[i][j] > arr[i][j+1]:
                            new_arr[i][j] -= m//4
                            new_arr[i][j+1] += m//4
                        else:
                            new_arr[i][j] += m//4
                            new_arr[i][j+1] -= m//4
            # 아래로 인접 체크 가능하면
            if i < N-1:
                if abs(arr[i][j]-arr[i+1][j]) >= 4:
                    nxt = (i+1)*M+j
                    # 둘 사이에 벽이 없다면
                    if 0 not in wall[i+1][j]:
                        m = max(arr[i][j], arr[i+1][j]) - min(arr[i][j], arr[i+1][j])
                        if arr[i][j] > arr[i+1][j]:
                            new_arr[i][j] -= m//4
                            new_arr[i+1][j] += m//4
                        else:
                            new_arr[i][j] += m//4
                            new_arr[i+1][j] -= m//4
    # 바깥 온도 감소
    for j in range(M):
        if new_arr[0][j] >= 1:
            new_arr[0][j] -= 1
        if new_arr[N-1][j] >= 1:
            new_arr[N-1][j] -= 1
    for i in range(1, N-1):
        if new_arr[i][0] >= 1:
            new_arr[i][0] -= 1
        if new_arr[i][M-1] >= 1:
            new_arr[i][M-1] -= 1

    # 초콜릿 섭취
    time += 1
    for ci, cj in check:
        if new_arr[ci][cj] < K:
            arr = new_arr
            break
    else:
        print(time)
        # print1(arr, pre_arr, new_arr)
        break
else:
    print(101)