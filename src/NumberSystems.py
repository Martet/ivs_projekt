"""!@package NumberSystems
    @brief A interface for conversions between binary and decimal.

    @date April 2021
"""

##  Converts decimal number to binary
#   @param num number to convert as string
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

##  Converts binary number to decimal
#   @param num number to convert as string
def BINTODEC(num):
    if not num.isnumeric():
        return ""
    return str(int(num, base=2))
