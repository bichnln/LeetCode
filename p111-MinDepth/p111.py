class TreeNode():
    __slots__ = "val", "left", "right"
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 
    

def minDepth(root: TreeNode) -> int:
    if root:
        # automatically make count to 1 if root exist
        count = 1
        # if this is the leaf node, return its count=1
        if not root.left and not root.right:
            return count
        # count depth of existing subtree
        elif not root.left or not root.right:
            if root.left:
                return count + minDepth(root.left)
            else:
                return count + minDepth(root.right)
        # left and right subtree exists
        else:
            minLeft = minDepth(root.left)
            minRight = minDepth(root.right)
            return min(minLeft, minRight) + count
    # this tree is None -> return 0
    else:
        return 0
        
def pathSum(root: TreeNode) -> int:
    if root:
        temp = root.val 
        if not root.left and not root.right:
            return temp 
    else:
        return 0