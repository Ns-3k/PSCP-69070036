"""3021"""
def main():
    """overlapcircle"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    d = (((x1-x2)**2)+((y1-y2)**2))**0.5
    if d < r1+r2:
        print("overlapping")
    else:
        print("no overlapping")
main()
