"""3129"""
def main():
    """coffee"""
    day = int(input())
    high = 0
    low = 2112
    avg = 0
    total = 0
    for _ in range (day):
        sale = int(input())
        if sale > high:
            high = sale
        if sale < low:
            low = sale
        total += sale
    avg = total/day
    print(f"{total}\n{high}\n{low}\n{avg:.1f}")
main()
