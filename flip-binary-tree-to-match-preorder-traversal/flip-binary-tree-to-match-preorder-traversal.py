class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        flips = []
        self.index = 1
        def helper(node):
            if node == None:
                return
            if node.left:
                if node.left.val == voyage[self.index]:
                    self.index += 1
                    helper(node.left)
                    if node.right == None:
                        return
                    if node.right.val != voyage[self.index]:
                        flips.append(-1)
                        return
                    self.index += 1
                    helper(node.right)
                    return
            if node.right:
                if node.right.val == voyage[self.index]:
                    if node.left:
                        flips.append(node.val)
                    self.index += 1
                    helper(node.right)
                    if node.left == None:
                        return
                    if node.left.val != voyage[self.index]:
                        flips.append(-1)
                        return
                    self.index += 1
                    helper(node.left)
                    return
            if node.left == None and node.right == None:
                return
            flips.append(-1)
        if voyage == []:
            return []
        if root.val != voyage[0]:
            return [-1]
        helper(root)
        print(flips)
        if -1 in flips:
            return [-1]
       
        return flips
        
                    
        