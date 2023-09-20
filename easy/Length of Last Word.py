def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    s = s[::-1]
    count = 0
    i = 0
    try:
        while count == 0 or s[i] != " ":

            if s[i].isalpha():
                count += 1
            i += 1
    except IndexError:
        return count
    return count

    # or just use return
    return len(s.split()[-1])

