class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = [0] * len(nums)
        tempind = 0

        for n in range(len(nums)):
            if nums[n] == 0:
                continue 
            else:
                temp[tempind] = nums[n]
                tempind +=1

        nums[:] = temp  
        