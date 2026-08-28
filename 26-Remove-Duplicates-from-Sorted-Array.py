class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writeptr = 1

        if not nums:
            return 0
        
        for readptr in range(1 ,len(nums)):
            if nums[readptr] != nums[readptr -1]:
                nums[writeptr] = nums[readptr]
                writeptr += 1
        
        return writeptr
        