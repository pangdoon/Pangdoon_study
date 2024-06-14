import heapq


# 시각을 계산하여 두 자릿수 형식으로 반환하는 함수
def format_time(hour, minute):
    return f"{hour:02d}:{minute:02d}"


def solution(n, t, m, timetable):
    # 크루 도착 시간을 분 단위로 변환하고 minitues 리스트에 저장
    minitues = []
    for time in timetable:
        hour, minute = map(int, time.split(":"))
        change_time = hour * 60 + minute  # 시간을 분 단위로 변환
        minitues.append(change_time)

    # 크루 도착 시간을 힙 구조로 변환하여 최소 힙으로 사용
    heapq.heapify(minitues)

    # 셔틀 도착 시각 계산 (첫 셔틀은 09:00이고, t분 간격으로 n회 운행)
    suttle_times = [540 + t * i for i in range(n)]  # 540은 09:00을 분 단위로 변환한 값

    # 마지막 셔틀에 콘이 탈 수 있는 가장 늦은 시각을 찾기
    for suttle_time in suttle_times:
        count = 0  # 현재 셔틀에 탑승한 크루 수
        # 셔틀 도착 시각까지 도착한 크루들을 셔틀에 태우기
        while minitues and minitues[0] <= suttle_time and count < m:
            last_crew = heapq.heappop(minitues)  # 가장 먼저 도착한 크루를 태움
            count += 1  # 탑승한 크루 수 증가

        if count < m:  # 셔틀에 자리가 남아 있는 경우
            con_time = suttle_time  # 콘은 셔틀 도착 시각에 맞춰 도착 가능
        else:  # 셔틀에 자리가 없는 경우, 마지막으로 탄 크루보다 1분 일찍 도착
            con_time = last_crew - 1

    # 계산된 시간을 "HH:MM" 형식으로 변환
    answer = format_time(con_time // 60, con_time % 60)
    print(answer)
    return answer


# 예제 테스트
solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03", "09:00"])
