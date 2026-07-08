class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        mx = nums[0]
        for i in range(1,len(nums)):
            current_max = max(nums[i], current_max+nums[i])
            mx = max(mx,current_max)
        return mx               
        