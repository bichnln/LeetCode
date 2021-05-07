from model import TreeNode
def isBalanced(root: TreeNode) -> bool:
    if root:
        if not root.left and not root.right:
            

def height(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        if not root.left and not root.right:
            return 0
        elif not root.right:
            return 1 + height(root.left)
        elif not root.left:
            return 1 + height(root.right)
        else:
            return 1 + max(height(root.left), height(root.right))

if __name__ == "__main__":
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(15)

    d = TreeNode(3)
    e = TreeNode(7)

    f = TreeNode(18)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.right = f

    print(height(a))
