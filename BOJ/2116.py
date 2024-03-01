import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_bottom(depth, up):  #아래를 찾아주는 함수
    global down

    for index in range(6):
        if dices[depth][index] == up:
            if index == 0:
                down = dices[depth][5]
            elif index == 1:
                down = dices[depth][3]
            elif index == 2:
                down = dices[depth][4]
            elif index == 3:
                down = dices[depth][1]
            elif index == 4:
                down = dices[depth][2]
            elif index == 5:
                down = dices[depth][0]
            return down



def dfs(depth, dices):
    global up
    global down

    mini_dice = []    # 초기화해주기
    up = down

    if depth == N:
        dice_count.append(mini_dice_count)
        return dice_count

    down = find_bottom(depth, up)
    for i in range(6):
        if dices[depth][i] != up and dices[depth][i] != down:
            mini_dice.append(dices[depth][i])

    mini_dice_count.append(max(mini_dice))
    dfs(depth + 1, dices)

N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]

# 마주 보는 경우가 3가지 경우가 있다. (A, F) // (B, D) // (C, E) //
# 첫째 줄을 예시로 보았을 때, (2, 4) // (3, 6) // (1, 5) // 이다.

#  우선 그렇게 따지면 for 문을 통해서 ..

down = 0
# 아래를 나타내 줄 변수
up = 0
# 위를 나타내 줄 변수

dice_count = []  # 주사위 아래 위치별로 최대값 모은 것들

for index in range(6):
    mini_dice_count = []  # 주사위 별 최대값
    mini_dice = []  # 주사위 값
    #첫번째 주사위의 위치를 정해줌
    if index == 0:
        down = dices[0][5]
    elif index == 1:
        down = dices[0][3]
    elif index == 2:
        down = dices[0][4]
    elif index == 3:
        down = dices[0][1]
    elif index == 4:
        down = dices[0][2]
    elif index == 5:
        down = dices[0][0]

    dfs(0, dices)

result = []
# 답을 도출해 줄 리스트
for dice_side in dice_count:
    result.append(sum(dice_side))

print(max(result))