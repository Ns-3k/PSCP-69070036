"""3020"""
def main():
    """coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    cap = 0
    bought = 0
    price = 0
    if not b:
        price = d*a
    else:
        while bought != d:
            if cap < b:
                price += a
                cap += 1
                bought += 1
            else:
                price += c
                cap -= b
                cap += 1
                bought += 1
    print(price)
main()
