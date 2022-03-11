'''
Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsDict = {}

        for i, v in enumerate(nums):
            if v not in numsDict.keys():
                numsDict.update({v: i})
            else:
                if abs(i - numsDict[v]) <= k:
                    return True
                else:
                    numsDict.update({v: i})

        return False
