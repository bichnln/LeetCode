class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def LowestCommonAncestor(root: TreeNode, q: TreeNode, p: TreeNode) -> TreeNode:
    if q.left == p or q.right == p:
        return q
    if p.left == q or p.right == q:
        return p 
    if root:
        if (root.left == q and root.right == p) or (root.left == p or root.right == q):
            return root 
        else:
            if q.val < root.val and p.val < root.val:
                return LowestCommonAncestor(root.left, q, p)
            elif q.val > root.val and p.val > root.val:
                return LowestCommonAncestor(root.right, q, p)
            else:
                return root
    

def sumToN(n: int) -> int:
    if n < 1:
        return 0
    else:
        return n + sumToN(n-1)

def change(n):
    n.append(6)

if __name__ == "__main__":
    # s = "anagram"
    # t = "nagaram"

    # print(sumToN(5))

    a = [1,2,3,4]
    n = a
    print(f"n: {n}, a: {a}")
    change(n)
    n = [1,2,3,4]
    print(f"n: {n}, a: {a}")