"""3238"""
def main():
    """elong ma"""
    x,k = input().split()
    x = int(x)
    text = ord(k)
    for i in range(x):
        for j in range(x):
            if (j == i or i+j == x-1) and k == "#":
                if j == x-1:
                    print("#")
                else:
                    print("#",end="")
            elif k == "#":
                if j == x-1:
                    print("-")
                else:
                    print("-",end="")
            if (j == i or i+j == x-1) and k != "#":
                if j == x-1:
                    print(chr(text+abs(i-2)))
                else:
                    print(chr(text+abs(i-2)),end="")
            elif k != "#":
                if j == x-1:
                    print("-")
                else:
                    print("-",end="")
main()
