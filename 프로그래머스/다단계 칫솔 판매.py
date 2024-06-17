def solution(enroll, referral, seller, amount):
    # 각 판매자의 수익을 저장할 리스트를 초기화
    answer = [0] * len(enroll)

    # 이름을 인덱스로 매핑하여 각 판매자의 위치를 쉽게 찾을 수 있도록 딕셔너리 생성
    graph = {name: idx for idx, name in enumerate(enroll)}

    # 각 판매자와 판매 금액을 순회
    for s, a in zip(seller, amount):
        revenue = a * 100  # 판매 금액을 100배로 변환
        current = s  # 현재 판매자를 초기화

        # 추천 체계를 따라 수익을 분배
        while current != "-" and revenue > 0:
            idx = graph[current]  # 현재 판매자의 인덱스를 찾음
            commission = revenue // 10  # 수수료는 수익의 10%
            answer[idx] += revenue - commission  # 수익에서 수수료를 제외한 금액을 현재 판매자의 수익에 추가
            revenue = commission  # 남은 금액은 수수료로 분배
            current = referral[idx]  # 추천인을 현재 판매자로 설정

    return answer  # 최종 수익을 반환


# 함수 호출 및 결과 출력
result = solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
)

print(result)  # 예상 결과: [360, 958, 108, 0, 450, 18, 180, 1080]
