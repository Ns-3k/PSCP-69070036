"""3392"""
def main():
    """arle-arle"""
    array = []
    for i in range(3):
        array.append(int(input()))
        print(f"Input number {i + 1} stored.")
    while True:
        choice = int(input())
        if choice == 1:
            print("Original order:", *array)
        elif choice == 2:
            print("Descending order:", *sorted(array, reverse=True))
        elif choice == 3:
            print("Ascending order:", *sorted(array))
        else:
            break
main()
