from model import TreeNode

def pathToLeaf(root: TreeNode) -> []: 
    if not root:
        return []
    elif not root.left and not root.right:
        return [str(root.val)]
    
    left = pathToLeaf(root.left)
    right = pathToLeaf(root.right)
    full = left + right
    result = []
    for i in full:
        result.append(str(root.val) + str(i))
    return result

def binaryToDec(num: str) -> int:
    dec = 0
    for i in range(len(num)-1, -1, -1):
        dec += pow(2, i)*int(num[i])
    return dec

def sumBinaryPath(arr: [str]) -> int:
    result = 0
    for i in arr:
        result += binaryToDec(i)
    return result
if __name__ == "__main__":

    

    print(binaryToDec("101"))
    print(sumBinaryPath(["1010", "0001","101"]))
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

    print(pathToLeaf(a))

    arr1 = [1,2,3,4,5]
    arr2 = [6,7,8,9]
    arr1 += arr2
    print(arr1)