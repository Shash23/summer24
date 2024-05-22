from typing import List, Optional

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    
    """
    Do not return anything, modify head in-place instead.
    """

    # find the middle node of the list

    slow_ptr = head

    #fast ptr
    fast_ptr = head

    while fast_ptr and fast_ptr.next:

        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    print(slow_ptr.val)
    
    
    #wurks
    
    # reverse the list from the slow_ptr to the fast_ptr
    
    prev, curr = None, slow_ptr
    
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
        
    #prev is now the head of the list
    
    print_list(head)
        
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

        
def listToLinkedList(arr: List[int]) -> Optional[ListNode]:
    
    if not arr:
        return None
    
    head = ListNode(arr[0])
    
    current = head
    
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head
        

test_cases = [
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5]
]

test_case  = [1, 2, 3, 4, 5]

head = listToLinkedList(test_case)
print(reorderList(head))




