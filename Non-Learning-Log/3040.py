"""3040"""
def main():
    """exchange"""
    money = int(input())
    ten = money//10
    money -= ten*10
    five = money//5
    money -= five*5
    two = money//2
    money -= two*2
    one = money
    print(f"10 = {ten}\n5 = {five}\n2 = {two}\n1 = {one}")
main()
