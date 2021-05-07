class TreeNode:
    __slots__ = "val", "left", "right"
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.right = right 
        self.left = left 


def maxDepth(root: TreeNode) -> int:
    if root:
        count = 1
        countLeft = maxDepth(root.left)
        countRight = maxDepth(root.right)
        if (countLeft > countRight):
            return count + countLeft 
        else:
            return count + countRight
    else:
        return 0

def PrintInorder(root: TreeNode):
    if root: 
        PrintInorder(root.left)
        print(root.val)
        PrintInorder(root.right)

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

    print(maxDepth(a))
