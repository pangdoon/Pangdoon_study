def dfs(count, mini_arr):
    # 종료 조건: count가 N일 때
    if count == N:
        return all_arr.append(mini_arr.copy())

    # 배열의 각 원소를 확인
    for k in range(len(arr)):
        if visited[k] == 0:
            visited[k] = 1
            mini_arr.append(arr[k])
            dfs(count + 1, mini_arr) # DFS 재귀 호출
            mini_arr.pop()  # Backtrack: 마지막 원소 제거하여 이전 상태로 돌아감
            visited[k] = 0  # 해당 원소 방문 해제

def find():
    global max_count

    # 모든 순열에 대해 계산
    for mini_arr in all_arr:
        count = 0
        for k in range(len(mini_arr)):
            if k < N - 1:
                count += abs(mini_arr[k] - mini_arr[k + 1])
        # 최댓값 갱신
        if max_count < count:
            max_count = count

N = int(input())

all_arr = []  # 모든 순열을 저장하는 리스트
mini_arr = []  # 현재 순열을 구성하는 리스트
arr = list(map(int, input().split()))  # 입력 배열
max_count = -987654321  # 최댓값 초기화
visited = [0] * N  # 방문 여부를 표시하는 리스트

dfs(0, mini_arr)  # DFS 호출로 모든 순열 생성
find()  # 생성된 순열에 대해 최댓값 계산

print(max_count)  # 최댓값 출력
