"""3065"""
def main():
    """roman"""
    num = int(input())
    if num < 0:
        print("Error : Please input positive number")
    elif not num:
        print("Error : Out of range")
    elif num <= 3:
        print("I"*num)
    elif num == 4:
        print("IV")
    elif num <= 8:
        print("V"+"I"*(num-5))
    elif num == 9:
        print("IX")
    else:
        print("Error : Out of range")
main()
