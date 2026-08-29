class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        nondup = set(sentence)

        if len(nondup) != 26:
            return False 
        
        return True