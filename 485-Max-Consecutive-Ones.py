class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currone = 0 
        maxone = 0

        for num in nums:
            if num == 1:
                currone +=1
                maxone = max(currone, maxone)
            else:
                currone = 0                
        
        return maxone  