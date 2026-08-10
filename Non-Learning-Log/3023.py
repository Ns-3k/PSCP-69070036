"""3023"""
def main():
    """calc"""
    n = int(input())
    press = 0
    if n == 1:
        print(1)
    else:
        for i in range(1,n+1):
            press += len(str(i))+1
        print(press)
main()
