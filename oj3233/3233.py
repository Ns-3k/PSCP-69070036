"""3233"""
def main():
    """lotto"""
    lotto1 = input()
    lotto2 = input()
    if lotto1 == lotto2:
        print(1000000)
    elif lotto1[0] != lotto2[0] and lotto1[2:] == lotto2[2:]:
        print(100000)
    elif lotto1[0] == lotto2[0] and lotto1[4:] == lotto2[4:]:
        print(2000)
    elif lotto1[0] == lotto2[0] and lotto1[5:] == lotto2[5:]:
        print(1000)
    elif lotto1[4:] == lotto2[4:]:
        print(200)
    elif lotto1[5:] == lotto2[5:]:
        print(100)
    elif lotto1[0] == lotto2[0]:
        print(20)
    else:
        print(0)
main()
