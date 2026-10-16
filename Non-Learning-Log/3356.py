"""3356"""
def main():
    """bussss"""
    row = int(input())
    col = int(input())
    seat = int(input())
    for j in range(row):
        if not j%2 and j > 0:
            print("")
        for i in range(1,col+1):
            if (row-j)+row*(i-1) == seat:
                print("XX",end=" " if i != col else "\n")
            else:
                if i != col:
                    print(f"{(row-j)+(row*(i-1)):02d}",end=" ")
                else:
                    print(f"{(row-j)+(row*(i-1)):02d}")
main()
