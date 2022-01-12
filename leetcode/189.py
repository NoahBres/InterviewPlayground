from typing import List


def isEven(n: int) -> bool:
    return n % 2 == 0


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or k == 0:
        return

    swaps = 0
    i = 0
    while swaps < len(nums):
        curr = i
        prev = nums[curr]

        while True and swaps < len(nums):
            nums[(curr + k) % len(nums)], prev = prev, nums[(curr + k) % len(nums)]
            curr += k

            swaps += 1

            if curr % len(nums) == i:
                i += 1
                break


list = [1, 2, 3, 4, 5, 6, 7]
rotate(list, 1)
print(list)
