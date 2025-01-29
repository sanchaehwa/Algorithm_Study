sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	
def solution(sizes):
    width = []
    height = []
    for i in sizes:
        width.append(max(i)) #[60,70,60,80] 
        height.append(min(i))#[50,30,30,40] 
    return (max(width) *max(height) )  #80 * 50
        
