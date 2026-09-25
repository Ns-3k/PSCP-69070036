"""3135"""
def main():
    """gift"""
    n,k,t = input().split(" ")
    n,k,t = int(n),int(k),int(t)
    check = set()
    for i in range (n):
        temp = 1+i*k
        if temp != n:
            temp %= n
        if temp in check:
            print(len(check))
            return
        check.add(temp)
        if temp == t:
            print(len(check))
            return
    print(len(check))
main()
