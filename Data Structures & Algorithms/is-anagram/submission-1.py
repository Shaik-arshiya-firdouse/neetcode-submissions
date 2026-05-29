class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        print(s1)
        t1=sorted(t)
        print(t1)
        if s1==t1:
            return True
        return False