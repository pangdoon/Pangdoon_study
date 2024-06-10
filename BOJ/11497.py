T = int(input())

for _ in range(1, T+1):
    N = int(input())
    tong_tree = list(map(int, input().split()))

    tong_tree.sort()   # 정렬을 해준다.

    left_tong_tree = []  # 왼쪽으로 넣기
    right_tong_tree = []   # 오른쪽으로 넣기

    for i in range(0,len(tong_tree),2):
        left_tong_tree.append(tong_tree[i])

    for i in range(1, len(tong_tree),2):
        right_tong_tree.append(tong_tree[i])

    right_tong_tree.sort(reverse=True)

    result = left_tong_tree + right_tong_tree    # 가장 크기 차이가 적게 통나무를 세워줌

    count = 0
    for i in range(len(result)):
        if i+1 <= len(result)-1:
            number = abs(result[i] - result[i+1])
            if count < number:
                count = number
        else:
            number = abs(result[i] - result[0])
            if count < number:
                count = number

    print(count)





