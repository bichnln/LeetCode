class TreeNode:
    __slots__ = "val", "left", "right"
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

def PrintInorder(root: TreeNode) -> None:
    if root:
        PrintInorder(root.left)
        print(root.val)
        PrintInorder(root.right)

def InvertBinaryTree(root: TreeNode) -> None:
    if root:
        
        if root.right and root.left:
            # case 1: both left and right exists
            temp = root.left
            root.left = root.right
            root.right = temp
            InvertBinaryTree(root.left)
            InvertBinaryTree(root.right)
            
        elif not root.right:
            # case 2: only left exists -> switch left to right, then keep inverting left's child branch
            root.right = root.left 
            root.left = None 
            InvertBinaryTree(root.right)
        elif not root.left:
            # case 3: only right exists -> switch right to left, then keep inverting right's child branch
            root.left = root.right 
            root.right = None 
            InvertBinaryTree(root.left)
    return root
if __name__ == "__main__":
    a = TreeNode(4)

    b = TreeNode(2)
    c = TreeNode(7)

    d = TreeNode(1)
    e = TreeNode(3)
    f = TreeNode(6)
    g = TreeNode(9)

    a.left = b 
    

    b.left = d
    b.right = e

    c.left = f
    c.right = g 

    InvertBinaryTree(a)
    PrintInorder(a)
