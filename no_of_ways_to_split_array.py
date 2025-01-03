class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n):
            nums[i] += nums[i-1]
        for i in range(n-1):
            if nums[i] >= (nums[n-1]-nums[i]):
                ans += 1
        return ans
