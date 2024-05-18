# N, M은 인풋으로 들어오는 값을 공백으로 구분하여 정수로 매핑된 값이 할당됨
N, M = map(int, input().split())
# 1 ~ N 까지의 숫자를 반복하면서 리스트에 초기 값으로 담음
lst = [i for i in range(1, N+1)]

# M번 반복하면서
for _ in range(M):
    # 람다식으로 x에서 1 뺀 값을 넣어줌
    i, j = map(lambda x:(int(x)-1), input().split())
    # 다음과 같이 작성해도 무방
    # i, j = map(int, input().split())
    # i, j = i-1, j-1
    # lst의 i번째와 j번째 값 변경(스위칭)
    lst[i], lst[j] = lst[j], lst[i]

print(*lst)