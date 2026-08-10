"""3066"""
def main():
    """sameๆ"""
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b == c:
        print("all the same")
    elif a != b != c and a != c:
        print("all different")
    else:
        print("neither")
main()
