"""3595"""
def main():
    """meteor"""
    a = float(input())
    b = float(input())
    c = float(input())
    count = 0
    meteor = 0
    while a >= c:
        a /= b
        meteor += b**count
        count += 1
    print(f"{meteor:.0f}")
main()
