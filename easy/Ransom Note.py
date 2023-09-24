from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    # ransomNote, magazine = sorted(ransomNote), sorted(magazine)
    # letter = 0
    # if len(ransomNote) > len(magazine): return False
    # if len(ransomNote) == 0: return True
    # for i in magazine:
    #     if ransomNote[letter] == i:
    #         letter += 1
    #         if letter == len(ransomNote):
    #             break
    # return letter == len(ransomNote)

    # st1, st2 = Counter(ransomNote), Counter(magazine)
    # return st1 & st2 == st1
    return Counter(magazine) >= Counter(ransomNote)



print(canConstruct(ransomNote = "12aab", magazine = "a1bba2bb1ba"))