#fees = [180,5000,10,600]
#records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
import math
#전처리 Key : 5961 Value : 시간  / 입출력
#{'5961' : ['05:34' , 'IN']}
# 동일한 Key 값에서 Out이 나오면 시간 계산하고 기본 시간이 넘었는지 아닌지에 따라 단위 요금 처리 


#전처리 코드
def solution(fees,records):
    #시간 / 자동차 번호 / 입출력 정보 
    #전처리 담을 dict
    car_records = {}
    total_time = {}
    for record in records:
        time, car_number , INOUT = record.split()
        #시간 전처리
        hour, minute = map(int,time.split(':'))
        time_split = (hour * 60)+ minute
        #만약에 car_number 이 car_records 에 없으면 -> 새로운 차
        if car_number not in car_records:
            car_records[car_number] = []
        car_records[car_number].append((time_split,INOUT))
    #print(car_records)
    #dict INOUT이 Out인지 봐야해 
    #car keys 
    for car_number,log in car_records.items():
        last_in = None
        total_time[car_number] = 0 
        for time,status in log:
            if status == 'IN':
                last_in = time
            elif status == 'OUT' and last_in is not None:
                total_time[car_number] += time - last_in
                last_in = None
        if last_in is not None:
            #23시 59분 
            last_time = (23 * 60) + 59
            total_time[car_number] += last_time - last_in
    #print(total_time)
    basic_time , basic_fee , time_min, time_fee = fees
    result = []
    for car_number in sorted(total_time.keys()):
        if total_time[car_number] <= basic_time:
            result.append(basic_fee)
        else:
            extra_time = total_time[car_number] - basic_time
            extra_fee = math.ceil(extra_time / time_min) * time_fee            
            result.append(basic_fee+ extra_fee)
    return result
#print(solution(records,fees))
