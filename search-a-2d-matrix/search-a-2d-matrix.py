class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) -1
        targetRow = None
        while low <= high:
            midIndex = (low + high) // 2
            mid = matrix[midIndex]
            if len(mid) == 0:
                return False
            if mid[0] > target:
                high = midIndex - 1
            elif mid[-1] < target:
                low = midIndex +1
            else:
                targetRow = midIndex
                break
        if targetRow == None:
            return False
        L = 0
        R= len(matrix[targetRow])-1
        targetAry = matrix[targetRow]
        while L <= R:
            mid = (L+R) // 2
            if targetAry[mid] == target:
                return True
            if targetAry[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False