def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    try:
        for _ in range((len(nums))):
            nums.remove(val)
    except ValueError:
        return len(nums)

    myList = []
    for i in range(len(nums)):
        if nums[i] != val:
            myList.append(nums[i])
    nums[:] = myList
    return len(myList)