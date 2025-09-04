from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        count = Counter(s)
        stack = []
        for char in s:
            count[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and count[stack[-1]] > 0 :
                stack.pop()
            stack.append(char)
        return ''.join(stack)
