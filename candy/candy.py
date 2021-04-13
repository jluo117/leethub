class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for index in range(len(ratings)):
            if index < 1:
                continue
            if ratings[index-1] < ratings[index]:
                candies[index] = max(candies[index],candies[index-1]+1)
        for index in range(len(ratings)-1,-1,-1):
            if index > len(ratings)-2:
                continue
            if ratings[index] > ratings[index+1]:
                candies[index] = max(candies[index],candies[index+1]+1)
        return sum(candies)