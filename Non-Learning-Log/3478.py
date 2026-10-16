"""3478"""
def main():
    """count123"""
    text = input()
    for char in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
        count = text.count(char)
        if count > 0:
            print(char, "=", count)
main()
