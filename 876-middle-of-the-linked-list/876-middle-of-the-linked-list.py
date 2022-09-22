# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        the_list_from_the_middle_Node=[]
        while head!=None:
            the_list_from_the_middle_Node.append(head)
            head=head.next
        return the_list_from_the_middle_Node[len(the_list_from_the_middle_Node)//2]
            
        