def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    half = len(nums // 2)
    arr = []
    for i in range(len(nums)):
        if nums[i] not in arr:
            if nums.count(nums[i]) > half:
                return nums[i]
        else:
            arr.append(nums[i])

# since the majority number will be present more than half of the
# array the number in the middle must be in the majority number
    nums.sort()
    n = len(nums)
    return nums[n//2]

print(majorityElement(nums=[2,2,1,3,1,1,4,1,1,5,1,1,6]))