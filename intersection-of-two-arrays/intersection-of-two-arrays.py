class Solution:
    def intersection(self, nums1, nums2):
        num1Set = set(nums1)
        nums2Set = set(nums2)
        res = []
        for val in num1Set:
            if val in nums2Set:
                res.append(val)
        return res
       
                        
                
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
