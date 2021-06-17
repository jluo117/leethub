class Solution:
    def numTeams(self, rating: List[int]) -> int:
        smallCount = [0] * len(rating)
        bigCount = [0] * len(rating)
        for lowerIndex in range(len(rating)):
            curSmall = 0
            curBig = 0
            for upperIndex in range(lowerIndex+1,len(rating)):
                if rating[lowerIndex] < rating[upperIndex]:
                    curBig += 1
                else:
                    curSmall += 1
            smallCount[lowerIndex] = curSmall
            bigCount[lowerIndex] = curBig
        count = 0
        for lower in range(len(rating)):
            for upper in range(lower+1,len(rating)):
                if rating[lower] < rating[upper]:
                    count += bigCount[upper]
                else:
                    count += smallCount[upper]
        return count
            
                