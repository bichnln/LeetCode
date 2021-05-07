from model import TreeNode 
def BFS(root: TreeNode) :
    if not root:
        return 
    queue = []

    queue.append(root)
    visited = []

    while len(queue) > 0:
        # print front of queue and remove it
        print(queue[0].val)
        node = queue.pop(0)
        visited.append(node.val)

        # enqueue left child of removed node - expand removed node
        if node.left:
            queue.append(node.left)    
        # enqueue right child 
        if node.right:
            queue.append(node.right)
    return visited
def leveling(bfsArray: []) -> [[int]]:
    result = []
    result.append([bfsArray[0]])
    bfsArray = bfsArray[1:]
    print(bfsArray)
    i = 1
    while len(bfsArray) > 0:
        result.append(bfsArray[:pow(2,i)])
        bfsArray = bfsArray[pow(2,i):]
        i += 1
    return result


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

    v = BFS(a)
    
    r = leveling(v)
    print(r)

