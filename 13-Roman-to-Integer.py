class Solution:
    def romanToInt(self, s: str) -> int:
        romannos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0
        n = len(s)

        while i < n:
            # Check if there is a next character and compare Roman numeral values
            if i + 1 < n and romannos[s[i]] < romannos[s[i + 1]]:
                total += romannos[s[i + 1]] - romannos[s[i]]
                i += 2  # Skip both characters
            else:
                total += romannos[s[i]]
                i += 1  # Move to next character

        return total