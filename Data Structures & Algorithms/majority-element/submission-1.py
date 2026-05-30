from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        indexes=Counter(nums)
        maxx=0
        for key,value in indexes.items():
            if value>maxx:
                maxx=value
                ans=key
        return ans

        