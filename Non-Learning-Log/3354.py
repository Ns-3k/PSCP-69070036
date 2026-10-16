"""3354"""
numlist = [0,1,2,3,4,5,6,7,8,9]
def main():
    """hinttt"""
    inlist = []
    for _ in range (3):
        inlist.append(input().split())
    ones = calc(inlist[0][0],int(inlist[0][1]))
    tens = calc(inlist[1][0],int(inlist[1][1]))
    hundreds = calc(inlist[2][0],int(inlist[2][1]))
    for i in hundreds:
        for j in tens:
            for k in ones:
                print(str(i)+str(j)+str(k))
def calc(sym,num):
    """calc"""
    match sym:
        case "==":
            return [num]
        case ">":
            return [i for i in numlist if i > num]
        case "<":
            return [i for i in numlist if i < num]
        case "<=":
            return [i for i in numlist if i <= num]
        case ">=":
            return [i for i in numlist if i >= num]
        case "!=":
            return [i for i in numlist if i != num]
main()
