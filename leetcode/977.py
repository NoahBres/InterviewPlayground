from typing import List
from collections import deque


def sortedSquares(nums: List[int]) -> List[int]:
    # Uses a queue for O(1) insertion at the head
    queue = deque()

    left = 0
    right = len(nums) - 1

    # O(n) solution
    while left <= right:
        lval = nums[left] ** 2
        rval = nums[right] ** 2

        if lval > rval:
            queue.appendleft(lval)
            left += 1
        else:
            queue.appendleft(rval)
            right -= 1

    return list(queue)


print(sortedSquares([-7, -3, 2, 3, 11]))
