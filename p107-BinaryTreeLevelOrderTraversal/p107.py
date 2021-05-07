class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

def bfs(root: TreeNode) -> [[int]]:
    queue = [root] 
    visited = [root]
    level = 0
    while queue:
        current = queue.pop(0)
        if get_children(current):
            for child in get_children(current):
                queue.append(child)
                visited.append(child)


    return visited

def get_children(root: TreeNode) -> [TreeNode]:
    if not root.left and root.right:
        return None 
    result = []
    if root.left: result.append(root.left)
    if root.right: result.append(root.right)
    return result
    



def PrintPreorder(root: TreeNode):
    if root:
        print(root.val)
        PrintPreorder(root.left)
        PrintPreorder(root.right)

            
    
    
        
if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    f = TreeNode(8)
    g = TreeNode(9)
    h = TreeNode(10)

    a.left = b
    a.right = c 

    c.left = d 
    c.right = e

    e.left = f
    f.left = g

    b.right = h

    # PrintPreorder(a)

    result = bfs(a)
    for i in result:
        print(i.val)

