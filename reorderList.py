# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast_ptr = head
        slow_ptr = head

        while fast_ptr and fast_ptr.next:

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # slow ptr will give way for the half way point
        
        prev, curr = None, slow_ptr

        while curr:

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # up til here is good
        first, second = head, prev

        while second.next:
            
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first, second = temp1, temp2

        return head