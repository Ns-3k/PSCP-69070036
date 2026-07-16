"""2992"""
def main():
    """swap"""
    num = input()
    opp = input()
    reverse = num[::-1]
    if opp == "*":
        print(f"{num} * {int(reverse)} = {int(num)*(int(reverse))}")
    else:
        print(f"{num} + {int(reverse)} = {int(num)+(int(reverse))}")
main()
