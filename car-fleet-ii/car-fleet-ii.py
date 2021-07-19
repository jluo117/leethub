class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def expected_collision_time(p1,s1,p2,s2):
            if s2>= s1:
                return -1
            return (p2-p1)/(s1-s2)
        collTime = [] 
        stk = []
        
        for p,s in reversed(cars):
            t = -1
            while len(stk):
                p2,s2,t2 = stk[-1]
                t = expected_collision_time(p,s,p2,s2)
                if s> s2 and (t <= t2 or t2 <0):
                    break
                else:
                    t = -1
                    stk.pop()
            stk.append((p,s,t))
            collTime.append(t)
        return collTime[::-1]