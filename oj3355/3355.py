"""3355"""
def main():
    """srtn"""
    temp = "yo"
    short = []
    num = []
    while temp != -1:
        temp = int(input())
        if not num or num[-1] - temp == -1:
            num.append(temp)
        else:
            if len(num) > 1:
                short.append(str(num[0])+"-"+str(num[-1]))
                num = [temp]
            else:
                short.append(*num)
                num = [temp]
    print(*short,sep=", ")
main()
