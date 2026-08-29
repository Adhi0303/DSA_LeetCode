class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left:int, right:int) -> int:
            palindromesFound = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromesFound += 1
                left -= 1 
                right += 1 

            return palindromesFound 

        for i in range(len(s)):
            count += expand(i , i)
            count += expand(i , i+1)
        
        return count 
        