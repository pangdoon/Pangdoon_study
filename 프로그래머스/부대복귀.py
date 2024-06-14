from collections import deque

def solution(n, roads, sources, destination):
    # 인접 리스트 생성
    road_connection = [[] for _ in range(n + 1)]
    for road in roads:
        road_connection[road[0]].append(road[1])
        road_connection[road[1]].append(road[0])

    # 최단 거리 계산을 위한 BFS
    distances = [-1] * (n + 1)  # 각 도시까지의 최단 거리를 저장하는 리스트
    distances[destination] = 0  # 목적지까지의 거리는 0
    queue = deque([destination])

    while queue:
        current = queue.popleft()
        current_distance = distances[current]

        for neighbor in road_connection[current]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 도시
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    # sources 리스트에 대해 각 도시의 최단 거리를 구함
    answer = [distances[source] for source in sources]

    return answer

# 예제 테스트
print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))  # 출력: [1, 2]


