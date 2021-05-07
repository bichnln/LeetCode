class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    
def hasPathSum(root: TreeNode, sum: int) -> bool: 
    if not root:
        return (sum == 0)
    else:
        result = False 
        subSum = sum - root.val 
        if subSum == 0 and not root.left and not root.right:
            return True 
        if root.left is not None:
            result = result or hasPathSum(root.left, subSum)
        if root.right:
            result = result or hasPathSum(root.right, subSum)
        
        return result

if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    f = TreeNode(8)
    g = TreeNode(9)
    h = TreeNode(10)

    a.left = b
    a.right = c 

    c.left = d 
    c.right = e

    e.left = f
    f.left = g

    b.right = h

    print(hasPathSum(a, 47))

    
        
