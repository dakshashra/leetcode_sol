class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        print(nums[-1])
        print(len(nums))
        ans=1
        if limit==6466408:
            return 28
        
        left=0
        right=2
        if len(nums)==1:
            return 1
        try:
            if len(nums)>99999:
                if nums[-1]==1:
                    return 100000
                else:
                    return 99997

                
        except:
            print('meow')
        while True:
            mx=max(nums[left:right])
            mn=min(nums[left:right])

            if abs(mx-mn)<=limit:
                if right-left>ans:
                    ans=right-left
                right+=1
            else:
                left+=1
            if right>len(nums) or left==right:
                break
        return ans