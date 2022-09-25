# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        if head==None:
            return head
        else:
            while current.next!=None: 
                if current.next.val==current.val:
                    self.deleteNode(current)
           
                else:
                    current=current.next
        return head
    def deleteNode(self, node):
        
        node.val=node.next.val
        node.next=node.next.next
        
