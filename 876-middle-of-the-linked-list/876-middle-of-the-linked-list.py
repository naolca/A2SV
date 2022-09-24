# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
         if not head:
            return
         length = 0
         node = head
        
         while node:#until the node is the tail
                
                node = node.next
                length += 1
            
         for i in range(length // 2):
            
            head = head.next#this loop ends when the head has the value of the middle element
        
         return head