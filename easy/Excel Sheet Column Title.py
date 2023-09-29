def convertToTitle(columnNumber: int) -> str:
    """
    :type columnNumber: int
    :rtype: str
    """
    # string = str(columnNumber)
    # aToz = {"1": "A","2": "B","3": "C","4": "D","5": "E","6": "F","7": "G","8": "H",
    #         "9": "I","10": "J","11": "K","12": "L","13": "M","14": "N","15": "O","16": "P",
    #         "17": "Q","18": "R","19": "S","20": "T","21": "U","22": "V","23": "W","24": "X",
    #         "25": "Y","26": "Z",}
    # # A -> 1 * A | AA - > 26 * A + 1 * A || AAA - > 260 * A + 26 * A + 1 * A
    # if string in aToz:
    #     return aToz[string]
    # if 701 >= columnNumber > 26:
    #     return f"{aToz[str(columnNumber // 26)]}{aToz[str(columnNumber % 26)]}"
    # elif 176462 > columnNumber > 701:
    #     return f"{aToz[str(columnNumber // 260)]}{aToz[str(columnNumber // 10 // 26)]}{aToz[str(columnNumber // 100 % 26)]}"
    #
    ans = []
    while columnNumber > 0:
        if columnNumber % 26 == 0:
            ans.append(chr(ord("A") + 25))
            columnNumber -= 1
        else:
            ans.append(chr(ord("A") + (columnNumber % 26) - 1))
        columnNumber //= 26

    return "".join(ans[::-1])

print(convertToTitle(701))