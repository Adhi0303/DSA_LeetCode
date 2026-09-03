class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversedwords = []

        for word in words:
            reversedword = word[::-1]
            reversedwords.append(reversedword)

        result = " ".join(reversedwords)

        return result