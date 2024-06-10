import heapq


def solution(n, works):
    answer = 0
    heapq_works = []
    for work in works:
        heapq.heappush(heapq_works, -work)

    print(heapq_works)

    return answer

solution(3, [3,2,1,2])