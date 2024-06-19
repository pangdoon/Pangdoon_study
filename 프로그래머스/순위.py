def solution(n, results):
    answer = 0

    # 상대방과의 승패를 파악할 수 있는 표를 생성
    # ranks[i][j]가 True이면 i가 j를 이긴 것, False이면 이긴 기록이 없음
    ranks = [[False] * (n + 1) for _ in range(n + 1)]

    # 결과를 통해 직접적인 승패 기록을 채움
    for A, B in results:
        ranks[A][B] = True  # A가 B를 이김

    # 플로이드-와샬 알고리즘을 사용하여 모든 선수들 간의 승패 관계를 파악
    # k는 중간에 거쳐가는 선수
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # 만약 i가 k를 이기고 k가 j를 이기면, i는 j를 이긴 것과 같음
                if ranks[i][k] and ranks[k][j]:
                    ranks[i][j] = True

    # 각 선수에 대해 다른 모든 선수와의 승패 관계가 확정된 선수를 찾음
    for i in range(1, n + 1):
        count = 0  # i 선수의 승패 관계가 확정된 선수의 수를 셈
        for j in range(1, n + 1):
            if ranks[i][j] or ranks[j][i]:
                count += 1
        # 자신을 제외한 모든 선수와의 승패 관계가 확정되었다면, 순위를 확정할 수 있음
        if count == n - 1:
            answer += 1

    return answer


# 주어진 예시 결과를 사용하여 함수 실행
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
