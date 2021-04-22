def DECTOBIN(num):
    if not num.isnumeric():
        return ""
    num = int(num)
    if num == 0:
        return "0"
    result = []
    while num > 0:
        result.insert(0, num % 2)
        num = num // 2
    return "".join(list(map(str, result)))

def BINTODEC(num):
    if not num.isnumeric():
        return ""
    return str(int(num, base=2))
