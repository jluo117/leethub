class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            while len(stk):
                if ast < 0 and stk[-1] > 0:
                    if abs(ast) > stk[-1]:
                        stk.pop()
                    elif abs(ast) == stk[-1]:
                        stk.pop()
                        ast = 0
                        break
                    else:
                        ast = 0
                        break
                else:
                    break
            if ast == 0:
                continue
            else:
                stk.append(ast)
        return stk
                
        