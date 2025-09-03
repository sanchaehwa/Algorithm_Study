
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx
            stack.append(idx)
        return result
