class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {nums[i]:i for i in range(len(nums))}
        
        for i in range(len(nums)):
            index = nums_dict.get(target - nums[i])
            if index and i != index:
                return [i, index]
