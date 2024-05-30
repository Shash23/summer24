from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:

            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True
    
    
this_set = {1,2,3}

print(this_set.add(4)) # prints none

print(this_set)