class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq=Counter(magazine)
        for ch in ransomNote:
            if ch in freq:
                if freq[ch]>0:

                    freq[ch]-=1
                else:
                    return False
            else:
                return False
        return True