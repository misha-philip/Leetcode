def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    pat = {}
    list1 = []
    list1[:0] = pattern
    list2 = list(s.split())
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] in pat:
            if list2[i] != pat[list1[i]]:
                return False
        elif list2[i] in pat.values():
            return False
        else:
            pat[list1[i]] = list2[i]
    return True
print(wordPattern(pattern = "abba", s = "dog cat cat dog"))