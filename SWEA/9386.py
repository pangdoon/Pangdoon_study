T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    max_count = 0
    count = 0
    for i in range(N):
        if arr[i] == 1:
            count += 1
            if i == (N - 1) and count > max_count:
                max_count = count

        elif arr[i] == 0:
            if count > max_count:
                max_count = count
            count = 0

    print(f"#{test_case} {max_count}")

