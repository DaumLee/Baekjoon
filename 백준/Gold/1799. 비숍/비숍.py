'''
모든 경우의 수 = 백트래킹으로 진행

아이디어
대각선끼리만 영향을 주니
i+j 가 짝수인 판과 i+j가 홀수인 판으로 구분해서 백트래킹 진행 후 각각 개수를 합쳐서 정답 출력

오답 이유
[1] 짝수 판에서 행이 넘어갈 때 조건을 홀수와 같이 둬서 잘못된 칸을 순회함
[2] N이 1일 때 홀수 칸이 없다는 점을 생각하지 못함
[3] \ 대각선을 구할 때 j-i의 절댓값이 아닌 값 자체를 넣어야한다고 중간에 알았는데 바꾸다 말아서 틀림
'''

# i+j가 홀수인 판
def odd(ci, cj, n, l, r):
    global odd_mx

    # 행이 넘어가면 최댓값 갱신
    if ci > N-1:
        odd_mx = max(odd_mx, n)
        return

    # 열이 범위 내면 2칸 옆으로
    if cj < N-2:
        ni, nj = ci, cj+2
    # 열이 범위 밖으로 나가면 다음 행으로
    else:
        ni, nj = ci+1, (ci+2) % 2

    # 보드에 올릴 수 있고, 좌대각선과 우대각선 상에 둘 수 있으면 선택
    if board[ci][cj] and ci+cj not in l and cj-ci not in r:
        odd(ni, nj, n+1, l+[ci+cj], r+[cj-ci])
    odd(ni, nj, n, l, r)


# i+j가 짝수인 판
def even(ci, cj, n, l, r):
    global even_mx

    # 행이 넘어가면 최댓값 갱신
    if ci > N-1:
        even_mx = max(even_mx, n)
        return

    # 열이 범위 내면 2칸 옆으로
    if cj < N-2:
        ni, nj = ci, cj+2
    # 열이 범위 밖으로 나가면 다음 행으로
    else:
        ni, nj = ci+1, (ci+1) % 2

    # 보드에 올릴 수 있고, 좌대각선과 우대각선 상에 둘 수 있으면 선택
    if board[ci][cj] and ci+cj not in l and cj-ci not in r:
        even(ni, nj, n+1, l+[ci+cj], r+[cj-ci])
    even(ni, nj, n, l, r)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

odd_mx = 0
even_mx = 0

# N이 2 이상이어야 홀수 칸 존재
if N > 1:
    # (0, 1)부터 진행
    odd(0, 1, 0, [], [])
# (0, 0)부터 진행
even(0, 0, 0, [], [])
print(odd_mx + even_mx)