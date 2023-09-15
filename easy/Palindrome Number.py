x = 23532
def is_x_palindrome(x):
    reversedx = str(x)[::-1]
    for i in range(len(str(x))):
        if str(x)[i] != reversedx[i]:
            return False
    return True

    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x //= 10
    return x == half or x == half // 10

    x = str(x)
    return x == x[::-1]