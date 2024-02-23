from collections import deque


# 종료 조건 확인, True면 종료
def check(lst):
    if lst.count(0) >= K:
        return False
    return True


def solve(lst):
    global ans

    step = 0
    # 로봇의 위치 저장
    robot = deque()

    while check(lst):
        step += 1
        # 다음 로봇의 위치 저장
        next = deque()
        # 컨베이어 작동
        lst = [lst[-1]] + lst[:-1]
        # 아래에서 로봇의 이동 중 이동하지 못한 로봇들의 위치
        now = []
        # 로봇 이동
        while robot:
            # 제일 앞에 있는 로봇부터 순회
            r = robot.popleft()
            # 로봇도 컨베이너와 함께 회전
            r += 1
            # 회전한 위치가 내리는 위치이면 그냥 내림
            if r == N-1:
                continue
            # 다음 칸으로 갈 수 있으면 이동하고 내구도 감소
            if lst[r+1] > 0 and r+1 not in now:
                lst[r + 1] -= 1
                # 다음 칸이 내리는 위치가 아니면 로봇은 컨베이너에 계속 있음
                if r+1 < N-1:
                    next.append(r+1)
            # 이동 못하면 그 위치에 그대로 있음
            else:
                now.append(r)
                next.append(r)
        # 시작지점의 내구도가 남아 있으면 로봇을 올림
        if lst[0] > 0:
            lst[0] -= 1
            next.append(0)
        # 로봇의 위치 최신화
        robot = next

    ans = step


N, K = map(int, input().split())
# 길이 = 2*N
con = list(map(int, input().split()))

# 정답
ans = 0

solve(con)

print(ans)