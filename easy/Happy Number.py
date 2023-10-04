
def isHappy(n: int):
    """
    :type n: int
    :rtype: bool
    """
    """arr = [int(i) for i in str(n)]
    for _ in range(10):
        n = sum(arr)
        if n == 1:
            return True
        arr = [int(i)**2 for i in str(n)]
    return False
        """
    hset = set()
    while n != 1:
        if n in hset: return False
        hset.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    else:
        return True


print(isHappy(19))
