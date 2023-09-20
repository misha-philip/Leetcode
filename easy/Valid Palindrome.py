def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = "".join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]

    # s = s.replace(",","").replace(".","").replace(":","").replace(" ","").lower()
    # return s == s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
