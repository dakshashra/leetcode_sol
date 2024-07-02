class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.pop(nums2.index(i))
        return ans