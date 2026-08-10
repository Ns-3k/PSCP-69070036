"""3027"""
def main():
    """fence"""
    fence = input().split(" ")
    price = int(input())
    lenght = ((int(fence[0])+int(fence[1]))*2)*int(fence[2])
    print(lenght)
    total = lenght*price
    print(total)
main()
