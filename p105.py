from model import TreeNode

def buildTree(preorder, inorder) -> TreeNode:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        if len(preorder) > 0 and len(inorder) > 0:
            
            root_val = preorder[0]
            root_index = inorder.index(root_val)
            leftPre = preorder[1:root_index]
            rightPre = preorder[root_index+1:]
            leftIn = inorder[:root_index]
            rightIn = inorder[root_index+1:]
            print(root_val,preorder, inorder, rightIn, leftIn, rightPre, leftPre)

            return TreeNode(root_val, buildTree(leftPre, leftIn), buildTree(rightPre, rightIn))

def inorderTraversal(root: TreeNode):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)
if __name__ == "__main__":
    preorder = [3,9,8,20,15,7,1,2,4]
    inorder = [8,9,3,15,20,7,2,4,1]
    a = buildTree(preorder, inorder)
    inorderTraversal(a)

