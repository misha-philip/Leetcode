from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # return Counter(t) <= Counter(s)
    # if len(s) != len(t):
    #     return False
    # seen = {}
    # for i in range(len(s)):
    #     seen[s[i]] = s.count(s[i])
    # for i in t:
    #     if i not in seen:
    #         return False
    #     if t.count(i) != seen[i]:
    #         return False
    # return True
    # if len(s) != len(t):
    #     return False
    # arr1 = {}
    # arr2 = {}
    # for i in s:
    #     if i in arr1:
    #         arr1[i] += 1
    #     else:
    #         arr1[i] = 1
    # for j in t:
    #     if j in arr2:
    #         arr2[j] += 1
    #     else:
    #         arr2[j] = 1
    # print(arr1, arr2)
    # if arr1 == arr2:
    #     return True
    # return False
    if len(s) != len(t):
        return False
    return sorted(t) == sorted(s)


print(isAnagram(s = "ccaa", t = "cacc"))
