from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for i, val in enumerate(nums):
            numDict[val] = i

        for i, val in enumerate(nums):
            currSub = target - val
            if currSub in numDict and numDict[currSub] != i:
                return [i, numDict[currSub]]
