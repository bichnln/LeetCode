class Node:
    def __init__(self, val=None, children = None):
        """ N-ary tree model """
        self.val = val 
        self.children = children
    
def postorderTraversal(root: Node) -> [int]:
    result = []
    if root:
        if not root.children:
            return [root.val]
        else:
            for i in root.children:
                result += postorderTraversal(i)
            result += [root.val]
    return result

def preorderTraversal(root: Node) -> [int]:
    result = []
    if root:
        result += [root.val]
        if root.children:
            for i in root.children:
                result += preorderTraversal(i)
    
    return result
