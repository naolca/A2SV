# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        if head==None:
            return True
        lst=[]
        while current:
            lst.append(current.val)
            current=current.next
        while lst:
            if head.val!=lst.pop():
                return False
            head=head.next
        return True
        

        
            
        