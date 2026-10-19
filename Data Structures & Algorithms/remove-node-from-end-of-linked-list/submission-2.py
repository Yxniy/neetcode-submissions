# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        

        slow = head
        curr = head
        for i in range(n):
            curr = curr.next
            
        if not curr:
            return head.next
        
        while curr.next:
            slow = slow.next
            curr = curr.next
        
        slow.next = slow.next.next
        
        return head