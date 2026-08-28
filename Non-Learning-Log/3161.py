"""3161"""
def main():
    """div 5"""
    num = int(input())
    for i in range(1,num+1):
        if i%5:
            print("*",end="")
        else:
            print("X",end="")
main()
