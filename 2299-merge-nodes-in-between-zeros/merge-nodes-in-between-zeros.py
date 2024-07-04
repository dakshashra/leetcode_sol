# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        m=head.next
        s=m
        while s:
            sum=0
            while s.val!=0:
                sum+=s.val
                s=s.next
            m.val=sum
            s=s.next
            m.next=s
            m=m.next
            
        return head.next