import sys
def is_acceptable(word: str) -> bool:
    vowels = set("aeiou")

    # 조건 1: 모음 하나 이상 포함
    if not any(ch in vowels for ch in word):
        return False

    # 조건 2: 모음 3개 또는 자음 3개 연속
    count = 1
    for i in range(1, len(word)):
        if (word[i] in vowels) == (word[i - 1] in vowels):  # 둘 다 모음이거나 둘 다 자음
            count += 1
            if count >= 3:
                return False
        else:
            count = 1  # 다른 종류면 카운트 초기화

    # 조건 3: 같은 글자 연속은 금지 (단, ee 와 oo는 예외)
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            if word[i] not in ['e', 'o']:
                return False
    return True
def solution(word:list):
    for lst in word:
        if is_acceptable(lst):
            print(f"<{lst}> is acceptable.")
        else:#false
            print(f"<{lst}> is not acceptable.")

word= []
while True:
    lst = sys.stdin.readline().strip()
    if lst == "end":
        break
    word.append(lst)
solution(word)