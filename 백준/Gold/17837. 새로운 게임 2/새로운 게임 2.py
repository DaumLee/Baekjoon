from collections import defaultdict

def solve(loc):
    time = 0
    # 칸마다 있는 말
    v = [[list() for _ in range(N)] for _ in range(N)]
    for i in range(1, K+1):
        si, sj = loc[i]
        v[si][sj].append(i)

    # 시간 조건 수정 (4시 12분)
    while time < 1000:
        time += 1
        # 1번 말부터 이동, 말은 K개 (4시 3분 추가)
        for num in range(1, K+1):
            ci, cj = loc[num]
            d = stone[num]
            di, dj = delta[d]
            ni, nj = ci+di, cj+dj
            # 흰 칸이나 빨간 칸으로 이동하려 하는 경우
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 2:
                for c in range(len(v[ci][cj])):
                    if v[ci][cj][c] == num:
                        move = v[ci][cj][c:]
                        # 좌표 이동 처리 추가 (4시)
                        for m in move:
                            loc[m] = (ni, nj)
                        # 빨간 칸
                        if arr[ni][nj]:
                            v[ni][nj].extend(move[::-1])
                        # 흰 칸
                        else:
                            v[ni][nj].extend(move)
                        v[ci][cj] = v[ci][cj][:c]
                        break
                # 이동이 끝나고 4개 이상이 한 칸에 있으면
                if len(v[ni][nj]) >= 4 or len(v[ci][cj]) >= 4:
                    return time
            # 범위를 벗어나거나 파란 칸으로 이동하려 하는 경우
            else:
                if d == 0:
                    stone[num] = 1
                elif d == 1:
                    stone[num] = 0
                elif d == 2:
                    stone[num] = 3
                else:
                    stone[num] = 2
                new_dir = stone[num]
                rdi, rdj = delta[new_dir]
                rni, rnj = ci+rdi, cj+rdj
                # 방향을 바꾸고 갈 수 없는 경우 자리에 가만히 있음
                if rni < 0 or rni >= N or rnj < 0 or rnj >= N or arr[rni][rnj] == 2:
                    continue
                for c in range(len(v[ci][cj])):
                    if v[ci][cj][c] == num:
                        move = v[ci][cj][c:]
                        # 좌표 이동 처리 추가 (4시)
                        for item in move:
                            loc[item] = (rni, rnj)
                        # 파란 칸을 만났는데 빨간 칸으로 이동하려는 경우 (4시 9분 추가)
                        if arr[rni][rnj]:
                            v[rni][rnj].extend(move[::-1])
                        else:
                            v[rni][rnj].extend(move)
                        v[ci][cj] = v[ci][cj][:c]
                        break
                # 이동이 끝나고 4개 이상이 한 칸에 있으면
                if len(v[rni][rnj]) >= 4 or len(v[ci][cj]) >= 4:
                    return time
    return -1

N, K = map(int, input().split())
# 체스판 색
arr = [list(map(int, input().split())) for _ in range(N)]
# 체스 말 (번호 : 방향)
stone = defaultdict(int)
# 체스 말의 위치 (말 번호는 1번부터 있기 때문에 맨 앞을 [0,0]으로 채움)
loc = [(0, 0)]
for i in range(1, K+1):
    si, sj, d = map(int, input().split())
    stone[i] = d-1
    loc.append((si-1, sj-1))
# 이동 방향 (동, 서, 북, 남)
delta = ((0, 1), (0, -1), (-1, 0), (1, 0))

print(solve(loc))