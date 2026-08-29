from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3
        counts = Counter(nums)
        result = []
        for val,freq in counts.items():
            if freq > threshold:
                result.append(val)
        
        return result
        