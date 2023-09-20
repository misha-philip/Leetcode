def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # O(n) solution
    if target <= nums[0]:
        return 0
    for i in range(len(nums) - 1):
        if nums[i] == target:
            return i
        if nums[i] < target <= nums[i+1]:
            return i + 1
    # return len(nums)
    '''
    # O(log n) solution
    if target < nums[0]:
        return 0
    if target > nums[len(nums) - 1]:
        return len(nums)
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end)/2
        if nums[mid] > target:
            end = mid - 1
            if end >= 0:
                if nums[end] < target:
                    return end + 1
            else:
                return 0
        elif nums[mid] < target:
            start = mid + 1
            if start < len(nums):
                if nums[start] > target:
                    return start
            else:
                return len(nums)
        else:
            return mid
    '''
    # better O(log n ) solution
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return l
