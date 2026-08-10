"""3039"""
def main():
    """min(loop)"""
    num = int(input())
    old = 10000000000000000000
    for _ in range(num):
        new = int(input())
        if new <= old:
            old = new
        else:
            pass
    print(old)
main()
