"""3068"""
def main():
    """calendar"""
    year = int(input())
    if year <= 1500 and not year%4:
        print("yes")
    elif not year%400:
        print("yes")
    elif not year%100:
        print("no")
    elif not year%4:
        print("yes")
    else:
        print("no")
main()
