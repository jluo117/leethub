class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def create_ary(p,q):
            p_demand = p[1]
            q_demand = q[1]
            min_val = min(p_demand,q_demand)
            product = p[0]*q[0]
            return [product,min_val],p[1]-min_val,q[1] - min_val
        e1_index = 0
        e2_index = 0
        res = []
        while e1_index < len(encoded1) and e2_index < len(encoded2):
            s,p_rem,q_rem = create_ary(encoded1[e1_index],encoded2[e2_index])
            
            if len(res) and res[-1][0] == s[0]:
                res[-1][1] += s[1]
            else:
                res.append(s)
            encoded1[e1_index][1] = p_rem
            encoded2[e2_index][1] = q_rem
            if encoded1[e1_index][1] == 0:
                e1_index += 1
            if encoded2[e2_index][1] == 0:
                e2_index += 1
        return res
        