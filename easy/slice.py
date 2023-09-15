nums = [2, 3, 4, 5]
target = 2
seen = {}
for i in range(len(nums)):
    diff = target - nums[i] # a + b = target / check if target - a = b has been seen b
    if diff in seen:
        print([seen[diff], i])
    else:
        seen[nums[i]] = i

seen = {}
for i in range(len(nums)):

    diff = nums[i] - target # a - b = target / if a - target = b
    if diff in seen:
        print(seen[diff], i)
    else:
        seen[nums[i]] = i

