"""3599"""
def main():
    """summ"""
    n = int(input())
    total = 0
    temp = 0
    while total != n and temp != -1:
        temp = int(input())
        if temp != -1:
            total += temp
    print(total)
main()
