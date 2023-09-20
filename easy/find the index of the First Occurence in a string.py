


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
     """
#     target = re.compile(needle)
#     match = re.search(target, haystack)
#     if match:
#         return match.span()[0]
#     else:
#         return -1
#
    # match = haystack.find(needle)
    # return match

    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


print(strStr("sadbutsad","lorem"))
