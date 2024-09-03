class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        sm=""
        for i in s:
            sm=sm+str(ord(i)-96)
        ans=0
        for i in range(k):
            
            for j in str(sm):
                ans+=int(j)
            sm=ans
            if i != k-1:
                ans=0
        return ans
