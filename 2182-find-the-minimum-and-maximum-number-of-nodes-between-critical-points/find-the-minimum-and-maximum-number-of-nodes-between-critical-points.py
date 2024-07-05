# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
        
        pos=[]
        curr=head
        nx=head.next
        try:
            wo=nx.next
        except:
            return ans
        c=1
        while wo:
            if (nx.val>curr.val and nx.val>wo.val) or (nx.val<curr.val and nx.val<wo.val):
                pos.append(c)
            c+=1
            curr=curr.next
            nx=nx.next
            wo=wo.next
        
        if len(pos)>=2:
            mn=pos[-1]
            for i in range(len(pos)-1):
                if pos[i+1]-pos[i]<mn:
                    mn=pos[i+1]-pos[i]
            return [mn,pos[-1]-pos[0]]
        else:
            pass
        
        return [-1,-1]