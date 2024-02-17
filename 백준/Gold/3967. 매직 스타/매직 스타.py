def solve(n, tlst):
    global flag

    # 사전 순으로 1회 정답 찾으면 종료
    if flag:
        return

    if tlst[0] + tlst[3] + tlst[6] + tlst[10] > 26:
        return

    if tlst[0] + tlst[2] + tlst[5] + tlst[7] > 26:
        return

    if tlst[1] + tlst[2] + tlst[3] + tlst[4] > 26:
        return

    if tlst[1] + tlst[5] + tlst[8] + tlst[11] > 26:
        return

    if tlst[4] + tlst[6] + tlst[9] + tlst[11] > 26:
        return

    if tlst[7] + tlst[8] + tlst[9] + tlst[10] > 26:
        return

    # 알파벳을 모두 채우면
    if n == 12:
        print(f'....{chr(tlst[0]+64)}....')
        print(f'.{chr(tlst[1]+64)}.{chr(tlst[2]+64)}.{chr(tlst[3]+64)}.{chr(tlst[4]+64)}.')
        print(f'..{chr(tlst[5]+64)}...{chr(tlst[6]+64)}..')
        print(f'.{chr(tlst[7]+64)}.{chr(tlst[8]+64)}.{chr(tlst[9]+64)}.{chr(tlst[10]+64)}.')
        print(f'....{chr(tlst[11]+64)}....')
        flag = 1
        return

    # 입력 값이 있는 칸은 그대로
    if o[n]:
        tlst[n] = o[n]
        solve(n+1, tlst)
    # 입력 값이 없는 칸은 쓰지 않은 알파벳을 사전순으로 대입
    else:
        for i in range(len(alp)):
            if not v[ord(alp[i])-64]:
                v[ord(alp[i])-64] = 1
                tlst[n] = ord(alp[i])-64
                solve(n+1, tlst)
                tlst[n] = 0
                v[ord(alp[i])-64] = 0


alp = [chr(i+65) for i in range(12)]
# 알파벳 별 사용 여부 체크
v = [0] * 13
# 매직스타 위에서부터 순서대로 배치한 배열
o = [0] * 12
# o 배열에 입력값을 차례로 삽입하기 위한 인덱스
idx = 0
for i in range(5):
    lst = list(input())
    for j in range(9):
        # 입력값에서 .은 출력을 위한 값이라 넘김
        if lst[j] != '.':
            # x는 채워야 하는 값
            if lst[j] == 'x':
                idx += 1
            # 입력된 값이 있으면 o 배열에 그대로 넣음
            else:
                o[idx] = ord(lst[j])-64
                # 해당 알파벳 방문처리
                v[ord(lst[j])-64] = 1
                alp.remove(lst[j])
                idx += 1


flag = 0
solve(0, [0]*12)