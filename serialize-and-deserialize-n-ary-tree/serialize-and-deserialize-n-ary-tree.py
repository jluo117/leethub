"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        curStr = ""
        if root == None:
            return ""
        def helper(root):
            if root == None:
                return []
            curRow = []
            curRow.append(root.val)
            for child in root.children:
                curRow.append(helper(child))
            return curRow
        return str(helper(root))
        
        
        
            
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
	
    def deserialize(self, data: str) -> 'Node':
        
        
        self.index = 1
        def converToAry():
            curAry = []
            while self.index < len(data)-1:
                if data[self.index] == '[':
                    self.index += 1
                    curAry.append(converToAry())
                    continue
                if data[self.index] == ']':
                    self.index += 1
                    return curAry
                curNum = ""
                while data[self.index] >= '0' and data[self.index] <= '9':
                    curNum += data[self.index]
                    self.index += 1
                if curNum:
                    curAry.append(int(curNum))
                if data[self.index] == ',':
                    self.index += 1
                    continue
                if data[self.index] == ' ':
                    self.index += 1
                    continue
            return curAry
        masterAry = converToAry()
        
        
        def helper(layer):
            if layer == []:
                return None
            curNode = Node(layer[0])
            curNode.children = []
            for val in layer:
                
                if isinstance(val, list):
                    curNode.children.append(helper(val))
                
                    
            return curNode
        return helper(masterAry)
                    
            
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))