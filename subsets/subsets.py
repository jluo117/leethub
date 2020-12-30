'''
2^3 
000-> []
001 -> [3]
010 -> [2]
011 -> [2,3]
100 -> [1]
101 -> [1,3]
110 -> [1,2]
111 -> [1,2,3]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            
            bitmask = bin(i)[3:]
            
            
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output
