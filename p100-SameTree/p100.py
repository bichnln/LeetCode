class TreeNode:
    __slots__ = "val", "left", "right"
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> None:
        """ Recursively check root node of each subtree until both is null or False found """
        # if both are null -> return true
        if not p and not q:
            return True

        # if only one of them is null -> False
        if not p or not q: 
            return False
        
        # if value is different -> False
        if p.val != q.val:
            return False 

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)



    