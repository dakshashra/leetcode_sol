class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l=[i for i in range(1, n+1)]
        x=0
        ll=len(l)
        cp=l
        for i in range(n-1):
            
            x+=(k-1)
            x=x%len(l)
            l.pop(x)
                
        return l[0]
