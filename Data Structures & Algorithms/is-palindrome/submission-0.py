import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=''.join(char for char in s if char not in string.punctuation)
        new=clean.replace(" ","") 
        newest=new.lower()
        if newest==newest[::-1]:
            return True
        return False