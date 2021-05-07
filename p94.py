from model import TreeNode
from typing import List, Optional

def inorderTraversal(root: TreeNode) -> List[int]:
    result = []
    if root:
        inorderTraversal(root.left)
        result += [root.val]
        inorderTraversal(root.right)
    return result 

