# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity : O(m+n)
        # Space complexity : O(1)
        dummy = ListNode(0)
        carry = 0
        cur1 = l1
        cur2 = l2
        cur = dummy
        while cur1 and cur2 :
            cur_sum = cur1.val + cur2.val + carry
            value = cur_sum % 10
            carry = cur_sum // 10
            new_node = ListNode(value)
            cur.next = new_node
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            cur_sum = cur1.val + carry
            value = cur_sum % 10
            carry = cur_sum // 10
            new_node = ListNode(value)
            cur.next = new_node
            cur = cur.next
            cur1 = cur1.next
            
        while cur2:
            cur_sum = cur2.val + carry
            value = cur_sum % 10
            carry = cur_sum // 10
            new_node = ListNode(value)
            cur.next = new_node
            cur = cur.next
            cur2 = cur2.next
        
        if carry:
            new_node = ListNode(carry)
            cur.next = new_node
        
        return dummy.next

            
