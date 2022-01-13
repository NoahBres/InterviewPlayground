from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeroBuffer = 0
    head = 0

    while head < len(nums):
        if nums[head] == 0:
            zeroBuffer += 1
        else:
            nums[head - zeroBuffer] = nums[head]

            nums[head - zeroBuffer + 1 : head + 1] = [0] * zeroBuffer

        head += 1


arr = [0]
moveZeroes(arr)
print(arr)
