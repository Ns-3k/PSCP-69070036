"""3014"""
def main():
    """milk"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        milk = d//a
    else:
        milk = d//a
        cap = milk
        while cap//b:
            if cap >= b:
                cap -= b-c
                milk += c
            else:
                break
    print(milk)
main()
