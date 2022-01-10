def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n

    while left < right:
        pivot = left + (right - left) // 2

        if isBadVersion(pivot):
            right = pivot
        else:
            left = pivot + 1

    return left
