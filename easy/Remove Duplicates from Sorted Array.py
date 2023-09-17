def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)
    # if we are not dealing with negative numbers if we do then change list() to sorted()
    nums[:] = list(set(nums))
    return len(nums)
