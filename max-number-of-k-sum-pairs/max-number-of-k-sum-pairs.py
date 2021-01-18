class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        visit = {}
        moves = 0
        for num in nums:
            if k - num in visit and visit[(k-num)] > 0:
                visit[k-num] -= 1
                moves += 1
            else:
                if num in visit:
                    visit[num] += 1
                else:
                    visit[num] = 1
        return moves
