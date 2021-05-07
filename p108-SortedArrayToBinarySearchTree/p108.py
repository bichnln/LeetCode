class TreeNode():
    __slots__ = "val", "left", "right"
    def __init__(self, val=0, left=None, right=None):
        self.val= val 
        self.left = left 
        self.right = right
    
def sortedArrayToBST( nums: []) -> int:    
    length = len(nums)
    root = TreeNode()
    if length == 0:
        root = None 
    elif length == 1:
        root = TreeNode(nums[0])
    elif length == 2:
        root = TreeNode(nums[1], TreeNode(nums[0]))
    elif length == 3:
        root = TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))
    else:
        rIndex = length//2
        lTree = nums[:rIndex]
        rTree = nums[rIndex+1:]
        root = TreeNode(nums[rIndex], sortedArrayToBST(lTree), sortedArrayToBST(rTree))
    return root

def PrintInorder(root: TreeNode):
    if root:
        PrintInorder(root.left)
        print(root.val)
        PrintInorder(root.right)

def PrintPreorder(root: TreeNode):
    if root:
        print(root.val)
        PrintPreorder(root.left)
        PrintPreorder(root.right)

if __name__ == "__main__":
    pass
    Seg = [-10, -3, 0, 5, 9]
    ex = [-3, 0, 5, 9]

    root = sortedArrayToBST(Seg)
 
    PrintPreorder(root)
