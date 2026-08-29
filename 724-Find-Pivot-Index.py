class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n

        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1]+nums[i]

        total_sum = prefix[-1]

        for i in range(n):
            leftsum = prefix[i] - nums[i]
            rightsum = total_sum - prefix[i]

            if leftsum == rightsum:
                return i
        
        return -1 
