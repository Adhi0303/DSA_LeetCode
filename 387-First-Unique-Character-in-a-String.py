class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freqarr = [0] * 26

        for char in s:
            freqarr[ord(char) - ord('a')] +=1
        
        for i in range(len(s)):
            if freqarr[ord(s[i]) - ord('a')] == 1 :
                return i
        
        return -1 

