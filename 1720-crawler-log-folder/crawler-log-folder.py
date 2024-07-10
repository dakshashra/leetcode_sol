class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=0
        for i in logs:
            if i[0] is not '.':
                ans+=1
            else:
                if len(i)==3:
                    ans=max(0, ans-1)
                else:
                    continue
        return ans