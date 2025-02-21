from collections import defaultdict
import math

def solution(fees, records):
    park_record = defaultdict(list)  # 차량별 입·출차 기록 저장
    result = []

    for record in records:
        Time, Car, Park = record.split()
        hour, min = map(int, Time.split(':'))
        time = hour * 60 + min
        park_record[Car].append((time, Park))

    total_times = {}

    for car, records in park_record.items():
        total_time = 0
        in_time = None
        
        for car_time, status in records:
            if status == 'IN':
                in_time = car_time
            elif status == 'OUT' and in_time is not None:
                total_time += car_time - in_time
                in_time = None 
        
        # 🚨 **출차 기록이 없는 경우 → 23:59(1439분) 출차 처리**
        if in_time is not None:
            total_time += (23 * 60 + 59) - in_time
        
        total_times[car] = total_time

    # 🚗 **요금 계산**
    for car in sorted(total_times.keys()):  # 차량 번호 오름차순 정렬
        total_time = total_times[car]
        
        if total_time <= fees[0]:  # 기본 시간 이하라면 기본 요금
            result.append(fees[1])
        else:  # 초과 시간 요금 계산
            extra_time = total_time - fees[0]
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]  # ⬅ 올림 적용
            result.append(fees[1] + extra_fee)

    return result  # 🔥 `return`을 추가

# ✅ 실행
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))  # 🔍 결과 확인