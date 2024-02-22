from itertools import permutations


# def check(lineup):
#     # 중복체크 배열
#     tmp = []
#     for i in lineup:
#         print(lineup, i)
#         tmp.append(lst_t[i])
#
#     # 이미 해당 타순과 같은 결과를 낼 수 있는 게임을 진행했으면
#     if tmp in arr:
#         return False
#     else:
#         arr.append(tmp)
#         return True


def game(lineup):
    lineup = list(lineup)
    lineup.insert(3, 0)
    global ans

    # 라인업으로 낼 수 있는 점수
    score = 0
    # 1번 타자부터 경기 시작
    b = 0
    # N이닝 동안
    for i in range(N):
        # 아웃카운트
        out = 0
        # 1, 2, 3루 베이스의 주자 초기화, base[3] = 득점
        base = [0, 0, 0, 0]
        while True:
            if lst[i][lineup[b]] == 0:
                out += 1
            elif lst[i][lineup[b]] == 1:
                # 3루 주자가 홈으로 이동
                base[3] += base[2]
                # 2루 주자가 3루로 이동
                base[2] = base[1]
                # 1루 주자가 2루로 이동
                base[1] = base[0]
                # 출루
                base[0] = 1
            elif lst[i][lineup[b]] == 2:
                # 2~3루 주자가 홈으로 이동
                base[3] += base[2] + base[1]
                # 1루 주자가 3루로 이동
                base[2] = base[0]
                # 출루
                base[1] = 1
                # 1루는 공석
                base[0] = 0
            elif lst[i][lineup[b]] == 3:
                # 기존 주자 모두 홈으로 이동
                base[3] += base[2] + base[1] + base[0]
                # 출루
                base[2] = 1
                # 1~2루는 공석
                base[1] = base[0] = 0
            else:
                # 타자와 주자 모두 홈으로 이동
                base[3] += base[2] + base[1] + base[0] + 1
                # 모든 베이스 초기화
                base[2] = base[1] = base[0] = 0
            # 타석이 끝나면 다음 타자가 들어오고
            b = (b+1) % 9
            # 3아웃이 되면 다음 이닝으로 넘어가면서 홈으로 들어온 점수 카운트
            if out == 3:
                score += base[3]
                break

    if ans < score:
        ans = score
        return


def solve(lineup):
    for i in permutations(lineup):
        # if check(i):
        game(i)


N = int(input())
# N 이닝 동안
lst = [list(map(int, input().split())) for _ in range(N)]
lst_t = list(zip(*lst))
# 9명 타순 처리했는지 확인
v = [0] * 9
# 점수
ans = 0
# 중복 체크 배열
arr = []
solve([1, 2, 3, 4, 5, 6, 7, 8])

print(ans)