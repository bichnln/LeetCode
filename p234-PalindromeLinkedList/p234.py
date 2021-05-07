class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = None 


def isPalindrome(head: ListNode) -> bool:
    if not head:
        return True 
    if not head.next:
        return True
    if head.next and not head.next.next:
        return False 
    
    fast = head
    slow = head
    count = 0
    odd = True
    temp = []

    while fast.next:
        temp.append(slow.val)
        if fast.next.next:
            fast = fast.next.next
        else:
            fast = fast.next
            odd = False
        slow = slow.next
        count += 1
    
    
    if odd:
        slow = slow.next
 

    while count > 0:
        if temp.pop() == slow.val:
            count -= 1
            slow = slow.next
        else:
            return False 
    return True  






if __name__ == "__main__":
    
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    m = ListNode(4)

    d = ListNode(3)
    e = ListNode(2)
    f = ListNode(1)

    a.next = b
    b.next = c 
    c.next = m

    m.next = d

    d.next = e  
    e.next = f

    print(isPalindrome(a))
