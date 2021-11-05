class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_set = {}
        for c in p:
            if c in p_set:
                p_set[c] += 1
            else:
                p_set[c] = 1
        
        L = 0
        R = len(p)
        cur_set = {}
        if len(s) < len(p):
            return []
        def same_set(target_set,check_set):
            for c in target_set:
                if c not in check_set:
                    return False
                if target_set[c] != check_set[c]:
                    return False
            return True
        for i in range(len(p)):
            if s[i] in cur_set:
                cur_set[s[i]] += 1
            else:
                cur_set[s[i]] = 1
        res = []
        if same_set(p_set,cur_set):
            res.append(0)
        while R < len(s):
            cur_set[s[L]] -= 1
            if s[R] in cur_set:
                cur_set[s[R]] += 1
            else:
                cur_set[s[R]] =1
            L += 1
            R += 1
            if same_set(p_set,cur_set):
                
                res.append(L)
        return res
        
        