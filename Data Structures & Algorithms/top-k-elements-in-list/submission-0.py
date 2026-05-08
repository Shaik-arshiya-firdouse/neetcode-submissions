from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        lst=[]
        sorted_dict=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))  
        keys=list(key for key,value in sorted_dict.items())
        return keys[:k]