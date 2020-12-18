class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resMap = {}
        stk = []
        for index in range(len(nums2)-1,-1,-1):
            while len(stk) > 0 and stk[-1] < nums2[index]:
                stk.pop()
            if len(stk) == 0:
                resMap[nums2[index]] = -1
            else:
                resMap[nums2[index]] = stk[-1]
            stk.append(nums2[index])
        res = []
        for num in nums1:
            res.append(resMap[num])
        return res
        
