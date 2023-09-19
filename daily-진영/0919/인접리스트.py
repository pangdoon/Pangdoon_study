arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]

# 이진 트리 만들기
nodes = [[] for _ in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(nodes[childNode])

# 자식이 더 이상 없다는 걸 표현하기 위해 None 을 삽힙
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None:
        return

    print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][0])
    preorder(nodes[nodeNumber][1])

preorder(1)