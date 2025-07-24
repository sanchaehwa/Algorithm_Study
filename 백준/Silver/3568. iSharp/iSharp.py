import sys
import re
input = sys.stdin.readline

t1 = input().strip().rstrip(';')  # 세미콜론 제거
tokens = t1.split()

base_type = tokens[0]  # int, double 등
variables = ' '.join(tokens[1:]).split(',')  # 변수들 ,로 분리

for v in variables:
    v = v.strip()
    name = ''
    suffix = ''
    for ch in v:
        if ch.isalpha():
            name += ch
        else:
            suffix += ch

    # 기호들만 따로 모아서 뒤집기 (주의: []는 묶어서 다뤄야 함)
    reversed_symbols = []
    i = len(suffix) - 1
    while i >= 0:
        if suffix[i] == ']':
            reversed_symbols.append('[]')
            i -= 2  # skip '['
        else:
            reversed_symbols.append(suffix[i])
            i -= 1

    result = base_type + ''.join(reversed_symbols) + ' ' + name
    print(result + ';')