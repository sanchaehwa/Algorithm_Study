#today = "2022.05.19"	
#terms = ["A 6", "B 12", "C 3"]
#privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]



#데이터 전처리
def date(t):
    Year, Month, Days = t.split('.')
    return (int(Year) * 12 * 28) + (int(Month) * 28) + int(Days)


def solution(today, terms, privacies):
    today_new = date(today)
    terms_new = {}
    answer = []
    for i in terms:
        a,b = i.split()
        terms_new[a]= int(b)*28
    
    for index,i in enumerate(privacies):
        
        a,b = i.split()
        dates = date(a)

        if b in terms_new:
            due = dates + terms_new[b]
            if today_new >= due:
                answer.append(index+1)

    return answer
#print(solution(today,terms,privacies))
