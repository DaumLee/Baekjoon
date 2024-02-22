from itertools import permutations


def play(lineup):
    lineup = list(lineup)
    # 라인업의 4번 타자는 1번 선수
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
        # 1, 2, 3루 베이스의 주자 초기화, base[0] = 득점
        base = [0, 0, 0, 0]
        while out < 3:
            if lst[i][lineup[b]] == 0:
                out += 1
            elif lst[i][lineup[b]] == 1:
                # 3루 주자 득점
                base[3] += base[2]
                # 타자와 주자 진루
                base[2], base[1], base[0] = base[1], base[0], 1
            elif lst[i][lineup[b]] == 2:
                # 2,3루 주자 득점
                base[3] += base[2] + base[1]
                # 타자와 주자 진루
                base[2], base[1], base[0] = base[0], 1, 0
            elif lst[i][lineup[b]] == 3:
                # 모든 주자 득점
                base[3] += base[2] + base[1] + base[0]
                # 타자 출루
                base[2], base[1], base[0] = 1, 0, 0
            else:
                # 타자와 주자 모두 득점
                base[3] += base[2] + base[1] + base[0] + 1
                # 모든 베이스 초기화
                base[2] = base[1] = base[0] = 0
            # 타석이 끝나면 다음 타자가 들어오고
            b = (b+1) % 9
        # 3아웃이 되면 다음 이닝으로 넘어가면서 홈으로 들어온 점수 카운트
        score += base[3]

    if ans < score:
        ans = score
        return


N = int(input())
# 이닝의 선수 별 성적
lst = [list(map(int, input().split())) for _ in range(N)]
# 선수의 이닝 별 성적
lst_t = list(zip(*lst))
# 최대 점수
ans = 0

# 1번 선수를 제외하고 순열 작성
for i in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    play(i)

print(ans)