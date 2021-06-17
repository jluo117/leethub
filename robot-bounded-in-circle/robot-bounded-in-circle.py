class Solution(object):
    def isRobotBounded(self, instructions):
        Foward = True
        Right = False
        Down = False
        Left = False
        pos = [0,0]
        for instruction in instructions:
            if instruction == 'G':
                if Foward:
                    pos[1] += 1
                if Right:
                    pos[0] += 1
                if Down:
                    pos[1] -= 1
                if Left:
                    pos[0] -= 1
            if instruction == 'L':
                if Foward:
                    Foward = False
                    Left = True
                    continue
                if Left:
                    Down = True
                    Left = False
                    continue
                if Down:
                    Right = True
                    Down = False
                    continue
                if Right:
                    Right = False
                    Foward = True
            if instruction == 'R':
                if Foward:
                    Foward = False
                    Right = True
                    continue
                if Left:
                    Foward = True
                    Left = False
                    continue
                if Down:
                    Left = True
                    Down = False
                    continue
                if Right:
                    Down = True
                    Right = False
                    continue
        return pos == [0,0] or Foward == False
                
                
        """
        :type instructions: str
        :rtype: bool
        """
        