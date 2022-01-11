from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        pivot = left + (right - left) // 2

        if nums[pivot] == target:
            return pivot
        else:
            if nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1

    return left


print(searchInsert([1, 3, 5, 6], 7))
