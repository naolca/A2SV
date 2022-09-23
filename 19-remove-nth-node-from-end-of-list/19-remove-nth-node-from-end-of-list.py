# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        # Move fast pointer n steps ahead
        for i in range(0, n):
            if fast.next is None:
                # If n is equal to the number of nodes, delete the head node
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next
        #the above loop executes until fast node reaches to the end
        # Next we will move both fast and slow pointers
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # next i remove the nth node from last element
        if slow.next is not None:
            slow.next = slow.next.next
        return head
        