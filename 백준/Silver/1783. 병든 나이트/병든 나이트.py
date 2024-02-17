N, M = map(int, input().split())

# N이 1이면 y이동이 불가능해서 시작점만 방문 가능
if N == 1:
    print(1)
# N이 2면
elif N == 2:
    # (-1, 2), (1, 2) 이동만 반복 가능, 칸수 제약
    if M <= 6:
        print((M+1)//2)
    # 4회를 넘으면 다른 방식의 이동이 불가능
    else:
        print(4)
# N이 3이면 모든 이동 가능
else:
    # 하다보니 안맞아서 손으로 그리니 경우의 수가 다음과 같음
    if M <= 3:
        print(M)
    elif M <= 5:
        print(4)
    # 최대 경로는 (-2, 1)과 (2, 1)을 반복적으로 이동하는 것, M-2회의 이동이 발생함
    else:
        print(M-2)