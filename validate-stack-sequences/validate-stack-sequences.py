class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        popIndex = 0
        for p in pushed:
            stk.append(p)
            while len(stk) and popped[popIndex] == stk[-1]:
                stk.pop()
                popIndex += 1
        return len(stk) == 0