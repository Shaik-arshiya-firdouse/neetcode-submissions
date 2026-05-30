class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}
        target=n/3
        ans=[]
        if n<=1:
            return nums
        else:
            for i in range(n):
                if nums[i] in freq:
                    freq[nums[i]]+=1
                else:
                    freq[nums[i]] = 1
            for key,value in freq.items():
                if value>target:
                    ans.append(key)
            return ans
                

        