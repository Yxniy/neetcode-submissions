class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        pointer = ans
        
        # 1. Loop only while BOTH contain data
        while list1 and list2:
            # We only need to check which is smaller. 
            # If they are equal, this logic will just pick list1, 
            # and pick list2 on the very next iteration.
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            
            # Move the result pointer forward
            pointer = pointer.next
        
        # 2. THE CLIFFHANGER FIX: Attach the remaining chain
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
            
        return ans.next