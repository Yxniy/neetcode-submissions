class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        pointer = ans
        carry = 0  # <--- Keep the carry here as a simple integer
        
        # Run while there are nodes left OR there is still a carry logic to process
        while l1 or l2 or carry:
            
            # 1. Get values (use 0 if the node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 2. Math
            total = val1 + val2 + carry
            carry = total // 10    # Get the new carry (e.g., 15 // 10 = 1)
            digit = total % 10     # Get the single digit (e.g., 15 % 10 = 5)
            
            # 3. Create the new node and attach it
            pointer.next = ListNode(digit)
            pointer = pointer.next
            
            # 4. Move input pointers forward (if they exist)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return ans.next