
def isIsomorphic(s: str, t: str) -> bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # if len(s) != len(t):
    #     return False
    # seens = {}
    # seent = {}
    # for i in s:
    #     if i in seens:
    #         seens[i] += 1
    #     else:
    #         seens[i] = 1
    # for x in t:
    #     if x in seent:
    #         seent[x] += 1
    #     else:
    #         seent[x] = 1
    # seen1 =[]
    # seen2 =[]
    # for i in seens:
    #     seen1.append(seens[i])
    # for x in seent:
    #     seen2.append(seent[x])
    # return seen1 == seen2
    # zip returns a tuple of mixed strings at each position of the strings
    # using sets to match the tuples if a char is in a different position
    # then the set of both will not remove it
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
    # Using hash map
    hashmap = {}
    for i in range(len(s)):
        # if s[i] has been seen
        if s[i] in hashmap:
            # check if this letter has been seen and if != from t[i]
            # means the letter is not in the same position as in s
            # there for it`s not isomorphic
            if hashmap[s[i]] != t[i]:
                return False
        # if not we enter it as key and give the value in same position t[i]
        else:
            hashmap[s[i]] = t[i]
    # if the there are double values means they are not morphic since the pos is different
    if len(set(hashmap.values())) != len(hashmap.values()):
        return False
    return True



print(isIsomorphic(s="paper", t="title"))
