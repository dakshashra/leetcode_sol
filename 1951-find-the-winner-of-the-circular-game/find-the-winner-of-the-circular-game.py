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
        while len(l)>1:
            
            x+=(k-1)
            x=x%len(l)
            print('poping', l[x%len(l)])       
            l.pop(x%len(l))
            print(l, 'x=', x)
                
        return l[0]
