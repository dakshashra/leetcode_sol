class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]

        for i in range(len(nums)):
            try:
                if (target-nums[i]) in nums:
                    
                    if i!=nums.index(target-nums[i]):
                        ans.append(i)
                        ans.append(nums.index(target-nums[i]))
                        ans.sort()
                        return ans
            except:
                pass
        return ans