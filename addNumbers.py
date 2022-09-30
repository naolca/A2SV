# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        
        head=ListNode((l1.val+l2.val)%10)
        carry=(l1.val+l2.val)//10
        
        if l1.next==None:
            if l2.next==None:
                head.next=ListNode(carry)
            return head
            l2.next=ListNode(carry)
        elif l2.next==None:
            l1.next=ListNode(carry)
        else:
            l1.next.va1+=carry
        head.next=self.addTwoNumbers(l1.next,l2.next)


        