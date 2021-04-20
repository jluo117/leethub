class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        person1 = []
        for slot in slots1:
            person1.append((slot[0],True))
            person1.append((slot[1],False))
        person1.sort()
        person2 = []
        for slot in slots2:
            person2.append((slot[0],True))
            person2.append((slot[1],False))
        person2.sort()
        p1 = 0
        p2 = 0
        p1Free = False
        p2Free = False
        lastFree = None
        while p1 < len(person1) and p2 < len(person2):
            if person1[p1][0] == person2[p2][0]:
                if p1Free and p2Free:
                    if lastFree + duration <= person1[p1][0]:
                        return [lastFree,lastFree+duration]
                p1Free = person1[p1][1]
                p2Free = person2[p2][1]
                
                if p1Free and p2Free:
                    lastFree = person2[p2][0]
                p1 += 1
                p2+= 1
                
            elif person1[p1][0] < person2[p2][0]:
                if p1Free and p2Free:
                    if lastFree + duration <= person1[p1][0]:
                        return [lastFree,lastFree+duration]
                p1Free = person1[p1][1]
                
                if p1Free and p2Free:
                    lastFree = person1[p1][0]
                p1 += 1
            else:
                if p1Free and p2Free:
                    if lastFree + duration <= person2[p2][0]:
                        return [lastFree,lastFree+duration]
                p2Free = person2[p2][1]
                
                if p1Free and p2Free:
                    lastFree = person2[p2][0]
                p2 += 1
        return []
            
                
                
        