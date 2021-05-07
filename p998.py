from model import TreeNode


def insertIntoMaxTree(root: TreeNode, val: int) -> TreeNode:
    if val > root.val:
        return TreeNode(val, root)
    else:
        if 
