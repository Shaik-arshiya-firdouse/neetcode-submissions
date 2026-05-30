class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::]==s[::-1]:
            return True
        else:
            for char in s:
                new = s.replace(char,"")
                print(new)
                if new[::]==new[::-1]:
                    return True
                new=""
                print(new)
        return False