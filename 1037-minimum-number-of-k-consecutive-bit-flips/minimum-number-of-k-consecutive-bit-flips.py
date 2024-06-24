class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flip_count = 0
        flip = 0
        is_flipped = [0] * n

        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]

            if nums[i] == flip:
                if i + k > n:
                    return -1
                is_flipped[i] = 1
                flip ^= 1
                flip_count += 1

        return flip_count
