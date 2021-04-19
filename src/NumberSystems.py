def NUMSYS(num, before, after):
    num=int(num,before)
    finish=[]
    while num > 0:
        finish.insert(0,num%after)
        num=num/after
    dictionary={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G"}
    for x in range(len(finish)):
        if dictionary.has_key(finish[x]):
            finish[x]=dictionary[finish[x]]
        else:
            finish[x]=str(finish[x])
    return "".join(finish)
def TO10(num, sys):
    if sys>0:
        int(num,sys)
    return num
