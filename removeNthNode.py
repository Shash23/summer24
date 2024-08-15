# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        slow_ptr, fast_ptr = head, head
        
        for i in range(n):
            fast_ptr = fast_ptr.next
            
        # if there are n elements and remove the nth node from the back
        if not fast_ptr:
            return head.next

        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
            
        slow_ptr.next = slow_ptr.next.next

        return head

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list back to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test the function
solution = Solution()

# Example test case
input_list = [1, 2, 3, 4, 5]
n = 2
head = create_linked_list(input_list)
new_head = solution.removeNthFromEnd(head, n)
output_list = linked_list_to_list(new_head)

print(f"Input: {input_list}, n = {n}")
print(f"Output: {output_list}")

# You can add more test cases here
