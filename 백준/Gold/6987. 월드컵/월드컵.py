from itertools import combinations


# 모든 팀의 게임 수가 5인지 체크
def game_check(lst):
    for i in range(0, 16, 3):
        if sum(lst[i:i+3]) != 5:
            return False
    return True


def solve(n, game, done):
    global ans

    if ans:
        return

    # 'A'팀 경기 완료
    if n == 5:
        if lst[:3] != game[:3]:
            return
    # 'B'팀 경기 완료
    elif n == 9:
        if lst[3:6] != game[3:6]:
            return
    # 'C'팀 경기 완료
    elif n == 12:
        if lst[6:9] != game[6:9]:
            return
    # 'D'팀 경기 완료
    elif n == 14:
        if lst[9:12] != game[9:12]:
            return
    # 전부 경기 완료
    elif n == 15:
        ans = 1
        return

    for t1, t2 in combinations(team, 2):
        if (t1, t2) in done:
            continue
        # t1이 더 승리할 수 있고 t2가 더 패배할 수 있으면
        if game[t1*3]+1 <= lst[t1*3] and game[t2*3+2]+1 <= lst[t2*3+2]:
            game[t1*3] += 1
            game[t2*3+2] += 1
            solve(n+1, game, done+[(t1, t2)])
            game[t1*3] -= 1
            game[t2*3+2] -= 1
        # 두 팀이 무승부일 수 있으면
        if game[t1*3+1]+1 <= lst[t1*3+1] and game[t2*3+1]+1 <= lst[t2*3+1]:
            game[t1*3+1] += 1
            game[t2*3+1] += 1
            solve(n+1, game, done+[(t1, t2)])
            game[t1*3+1] -= 1
            game[t2*3+1] -= 1
        # t1이 더 패배할 수 있고 t2가 더 승리할 수 있으면
        if game[t1*3+2]+1 <= lst[t1*3+2] and game[t2*3]+1 <= lst[t2*3]:
            game[t1*3+2] += 1
            game[t2*3] += 1
            solve(n+1, game, done+[(t1, t2)])
            game[t1*3+2] -= 1
            game[t2*3] -= 1
        # t1, t2가 게임 진행이 불가능하면 실패
        else:
            return


for _ in range(4):
    lst = list(map(int, input().split()))
    w = []
    d = []
    l = []
    for i in range(18):
        # 승
        if i % 3 == 0:
            w.append(lst[i])
        elif i % 3 == 1:
            d.append(lst[i])
        else:
            l.append(lst[i])

    team = [i for i in range(6)]
    ans = 0
    idx = 0
    if not game_check(lst):
        print(0, end=' ')
    elif sum(w) != sum(l):
        print(0, end=' ')
    elif sum(d) % 2:
        print(0, end=' ')
    else:
        solve(0, [0]*18, [])
        print(ans, end=' ')