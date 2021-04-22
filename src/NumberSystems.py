def NUMSYS(num):
    sys=2
    result=[]
    while num > 0:
        result.insert(0,cislo%sys)
        num=num/sys
    return "".join(result)
def TO10(num, sys):
    if sys>0:
        int(num,sys)
    return num
