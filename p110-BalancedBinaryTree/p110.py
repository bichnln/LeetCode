class TreeNode():
    __slots__ = "val", "left", "right"
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
    
def isBalancedBinaryTree(nums: [int]) -> bool:
    

if __name__ == "__main__":
    print(isBalancedBinaryTree([1, 2]))