#n : 택배 상자 개수 , w : 가로로 놓는 상자의 개수 , num : 꺼내려는 택배 상자의 번호 (-> target)

def solution(n, w, num):
    
    # 왼 --> 오 (증가) / 오 --> 왼 (감소) : 오른쪽 방향 으로 w개 만큼 두면 방향을 바꿔서 왼쪽 방향으로 w개 만큼 두면 되지
    #전체 상자 놓는 리스트
    boxs = [[] for _ in range(w)]
    #상자번호
    box_num = 0
    #방향
    direction = 1 #오른쪽 방향
    
    while box_num < n:
        for idx in range(0,w,direction) if direction == 1 else range(w-1,-1,-1):
            box_num += 1
            boxs[idx].append(box_num)
            if box_num == n: #모든 박스를 다 돌았다는거
                break
        direction *= -1 #방향 전환
    
    for values in boxs: #[1,12,13] / [2,11,14] / [3,10,15]
        if num in values:
            return len(values) - values.index(num) #꺼내야할 상자개수 앞에서부터 꺼내야함
