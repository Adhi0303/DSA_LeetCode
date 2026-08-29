class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        maxlen = 1
        currlen = 1

        for i in range(len(nums) -1):
            if nums [i] < nums[i+1]:
                currlen += 1
                maxlen = max(maxlen, currlen)
            else:
                currlen = 1
        
        return maxlen