class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        Lmost = float('inf')
        Rmost = -float('inf')
        pSet = set()
        for point in points:
            Lmost = min(Lmost,point[0])
            Rmost = max(Rmost,point[0])
            pSet.add(tuple(point))
        midPoint = (Lmost+Rmost)/2
        for i in points:
            if (midPoint + (midPoint - i[0]), i[1]) not in pSet:
                return False
        return True