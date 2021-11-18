class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        res = 0
        for index in range(len(nums1)):
            res += nums1[index] * nums2[len(nums2)-(1+index)]
        return res
        