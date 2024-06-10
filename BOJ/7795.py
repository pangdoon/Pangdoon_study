import sys
input = sys.stdin.readline

T = int(input())   # 테스트 케이스

for _ in range(1, T+1):   # 테스트 케이스 만큼 돌려줌
    N, M = map(int, input().split())   # N, M을 받음
    A = list(map(int, input().split()))
    B = list(map(int, input(). split()))

    count = 0   # 답을 나타내어 줄 것.

    A.sort(reverse=True)
    B.sort()

    for num1 in A:
        for num2 in B:
            if num2 >= num1:
                break
            else:
                count += 1

    print(count)