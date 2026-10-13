# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        nsecond = head

        # 1. Create the gap of size 'n'
        for i in range(n):
            nsecond = nsecond.next 
        
        # EDGE CASE CHECK:
        # If nsecond is None, it means n equals the list length.
        # We need to remove the HEAD.
        if not nsecond:
            return head.next
        
        # 2. Slide the window until 'nsecond' hits the very last node
        while nsecond.next:
            first = first.next
            nsecond = nsecond.next
            
        # 3. Perform the deletion
        # 'first' is now just before the node we want to remove
        first.next = first.next.next
        
        return head