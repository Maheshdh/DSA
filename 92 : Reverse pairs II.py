# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Time complexity : O(n)
        # Space complexity : O(1)
        
        # move pointer to left node
        dummy = ListNode(0, head)
        cur = head
        left_node = dummy
        for i in range(left-1):
            left_node = cur
            cur = cur.next
        
        # reverse r - l + 1 nodes
        prev = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # re - structure
        left_node.next.next = cur
        left_node.next = prev

        return dummy.next
