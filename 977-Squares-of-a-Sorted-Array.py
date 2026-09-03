class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left = 0
        right = n-1
        pos =n-1

        while left <= right:
            leftsq = nums[left] * nums[left]
            rightsq = nums[right] * nums[right]

            if leftsq > rightsq:
                result [pos] = leftsq
                left += 1
            else:
                result[pos] = rightsq
                right -= 1
            
            pos -= 1
        
        return result 
        