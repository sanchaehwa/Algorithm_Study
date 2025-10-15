import sys
input = sys.stdin.readline

def find_H(N,M,tree):
    st = 0
    en = tree[-1]
    answer = 0
    while st <= en: 
        md = (st + en) // 2
        cut_length = md
        m_count = 0
        for t in tree:
            if cut_length <= t:
                m_count += (t - cut_length)
        if m_count < M:
            en = md - 1
        elif m_count >= M:
            answer = max(answer,cut_length)
            st = md + 1
    return answer



N,M = map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()
print(find_H(N,M,tree))
