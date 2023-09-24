def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i, j = 0, 0
    # while s is not "" and t not "" lets try to see subsequence
    while i < len(s) and j < len(t):
        # if we start to match from the first letter
        if s[i] == t[j]:
            # increment i and search for  the nex sequence in the string
            i += 1
        # increment j to continue going through the sequence
        j += 1
    # if all the sequences of the string were found then i will be as
    # the len of the string
    return i == len(s)

    if len(s) > len(t): return False
    if len(s) == 0: return True
    sub = 0
    for i in range(len(t)):
        if sub < len(s):
            if s[sub] == t[i]:
                sub += 1
        else:
            return sub == len(s)
    return sub == len(s)


print(isSubsequence(s = "asd", t = "asadsfgsgd"))
