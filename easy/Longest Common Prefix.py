def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for let in range(min(len(first), len(last))):
        if(first[let] != last[let]):
            return ans
        ans += first[let]
    return ans
