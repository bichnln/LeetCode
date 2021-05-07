from model import TreeNode 

def MaximumBinaryTree(arr: []) -> TreeNode:
    if len(arr) == 1:
        return TreeNode(arr[0])
    elif len(arr) > 1:
        rootIndx = arr.index(max(arr))

        leftArr = arr[:rootIndx]
        rightArr = arr[rootIndx+1:]
        return TreeNode(arr[rootIndx], MaximumBinaryTree(leftArr), MaximumBinaryTree(rightArr))
    else:
        return None
    
def InorderTraversal(root: TreeNode):
    if root:
        InorderTraversal(root.left)
        print(root.val)
        InorderTraversal(root.right)
def PreorderTraversal(root: TreeNode):
    if root:
        print(root.val)
        PreorderTraversal(root.left)
        PreorderTraversal(root.right)
if __name__ == "__main__":
    a = [3,2,6,1]
    result = MaximumBinaryTree(a)
    PreorderTraversal(result)

    