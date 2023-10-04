def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    seen = {}
    i = 0
    for x in nums:
        if x in seen:
            if abs(seen[x] - i) <= k:
                return True
            seen[x] = i
        else:
            seen[x] = i
        i += 1
print(containsNearbyDuplicate(nums = [1,0,2,3,1,1], k = 3))
