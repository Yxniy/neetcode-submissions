class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1. Start both at the starting line
        slow = head
        fast = head
        
        # 2. Run as long as the Fast runner has track ahead
        while fast and fast.next:
            
            # Move first!
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            # Check for collision AFTER moving
            # strictly compare the NODE, not the value (.val)
            if slow == fast:
                return True
                
        return False