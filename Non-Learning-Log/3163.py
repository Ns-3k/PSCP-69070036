"""3163"""
def main():
    """stock"""
    item = int(input())
    total = 0
    even = 0
    odd = 0
    for _ in range (item):
        stock = int(input())
        total += stock
        if not stock%2:
            even += 1
        else:
            odd += 1
    print(f"SUM {total}\nEVEN {even}\nODD {odd}")
main()
