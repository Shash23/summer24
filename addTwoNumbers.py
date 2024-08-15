def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    carry = 0
    res = ListNode(0)
    dummy = res
    
    while l1 or l2 or carry != 0:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        
        total = l1_val + l2_val + carry
        carry = total // 10
        
        total_node = ListNode(total % 10)
        dummy.next = total_node
        dummy = dummy.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return res.next
        
        