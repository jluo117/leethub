class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        table = {}
        def helper(index):
            if index == len(books):
                return 0
            if index in table:
                return table[index]
            curWidth = 0
            rowMax = 0
            minNeeded = float('inf')
            for i in range(index,len(books)):
                if curWidth + books[i][0] > shelf_width:
                    minNeeded = min(minNeeded,helper(i) + rowMax)
                    break
                curWidth += books[i][0]
                rowMax = max(rowMax,books[i][1])
                minNeeded = min(minNeeded,helper(i+1)+rowMax)
            table[index] = minNeeded
            return minNeeded
        return helper(0)
