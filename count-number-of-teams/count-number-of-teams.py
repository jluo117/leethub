'''
[2,5,3,4,1]
3n
//2,1  //2,2 //



'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        decHelper = {}
        incHelper = {}
        def incHelp(rem,index):
            if rem == 0:
                return 1
            if (rem,index) in incHelper:
                return incHelper[(rem,index)]
            res = 0
            for upperIndex in range(index+1,len(rating)):
                if rating[upperIndex] > rating[index]:
                    res +=  incHelp(rem-1,upperIndex)
            incHelper[(rem,index)] = res
            return res
        def decHelp(rem,index):
            
            if rem == 0:
                
                return True
            if (rem,index) in decHelper:
                return decHelper[(rem,index)]
            res = 0
            for upperIndex in range(index+1,len(rating)):
                if rating[upperIndex] < rating[index]:
                    res +=  decHelp(rem-1,upperIndex)
                        
            decHelper[(rem,index)] = res
            return res
        pos = 0
        for index in range(len(rating)):
            pos += incHelp(2,index)
            pos += decHelp(2,index)
        return pos
            
            