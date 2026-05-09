class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lst = list(set(nums))
        ans=[]
        for l in lst:
            if nums.count(l) > (len(nums)//3):
                ans.append(l)
        return ans

        