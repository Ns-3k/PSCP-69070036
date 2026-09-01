"""3157"""
def main():
    """score"""
    num = int(input())
    total = 0
    for _ in range (num):
        sign = input()
        if sign == "+":
            total += 10
        else:
            total -= 5
    print(total)
main()
