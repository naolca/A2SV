# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create obj to b returned
        ans=ListNode()
        s1,s2=[],[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        carry=0
        while s1 or s2 or carry:
            summation = carry
            if s1: summation += s1.pop()
            if s2: summation += s2.pop()
            carry=summation//10
            summation%=10
            ans.val = summation
            temp = ListNode()
            temp.next = ans
            ans = temp
        return ans.next


            

        
