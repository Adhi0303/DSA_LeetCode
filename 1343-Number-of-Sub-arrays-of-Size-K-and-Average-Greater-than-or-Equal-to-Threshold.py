class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetsum = k * threshold

        cursum = sum(arr[:k])
        count = 0

        if cursum >= targetsum:
            count += 1

        for i in range(k, len(arr)):
            cursum += arr[i] - arr[i - k]

            if cursum >= targetsum:
                count += 1 
        return count 