class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=['_']*len(nums)
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr[i] = nums[i]
                print(arr)
            else:
                return True
        return False
