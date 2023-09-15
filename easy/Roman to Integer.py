

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = []
    exception = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    while len(s) >= 2:

        if s[0] + s[1] in exception:
            number.append(exception[(s[0] + s[1])])
            s = s[2:]

        else:
            number.append(roman[s[0]])
            s = s[1:]
    if s != "":
        number.append(roman[s[0]])
    return sum(number)


    s = s.replace("IV", "IIII","IX", "VIIII","XL", "XXXX","XC", "LXXXX","CD", "CCCC","CM", "DCCCC")
    sum = 0
    for char in s:
        sum += roman.get(char)
    return sum


    ans = 0

    # len(s) -1 cause for last value will be IndexError
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i + 1]]:
            ans -= roman[s[i]]
        else:
            ans += roman[s[i]]

    # adding last Value and return ans in int
    return ans + roman[s[-1]]