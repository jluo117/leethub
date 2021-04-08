class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        pos = []
        for res in restaurants:
            if veganFriendly and res[2] == 0:
                continue
            if maxPrice >= res[3] and maxDistance >= res[4]:
                pos.append((-res[1],-res[0]))
        pos.sort()
        return [-val[1] for val in pos]
    
            