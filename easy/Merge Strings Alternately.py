def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    merged = []
    for i in range(len(word1) + len(word2)):
        try:
            merged.append(word1[i])
        except IndexError:
            pass
        try:
            merged.append(word2[i])
        except IndexError:
            pass
    return "".join(merged)

    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return "".join(result)
