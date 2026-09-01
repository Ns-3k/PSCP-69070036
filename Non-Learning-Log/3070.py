"""3070"""
def main():
    """odd/even"""
    odd = 0
    even = 0
    for _ in range(3):
        num = int(input())
        if num%2 :
            odd += 1
        else:
            even += 1
    print(f"{even}\n{odd}")
main()
