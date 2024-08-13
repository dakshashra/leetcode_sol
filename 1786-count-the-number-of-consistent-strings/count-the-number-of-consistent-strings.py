class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        for i in words:
            flag=0
            for j in i:
                if j in allowed:
                    pass
                else:
                    flag=-1
            if flag==0:
                ans+=1
                
        return ans