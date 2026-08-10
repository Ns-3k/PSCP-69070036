"""3018"""
def main():
    """rectangle"""
    rec1 = input().split(" ")
    rec2 = input().split(" ")
    x1 = int(rec1[0])
    y1 = int(rec1[1])
    w1 = int(rec1[2])
    h1 = int(rec1[3])
    x2 = int(rec2[0])
    y2 = int(rec2[1])
    w2 = int(rec2[2])
    h2 = int(rec2[3])
    if  x1+w1 <= x2 or y1+h1 <= y2:
        print("no overlapping")
    elif w1 <= w2 :
        if y1 <= y2 :
            print((w1-abs(x1-x2))*(h1-abs(y1-y2)))
        else :
            print((w1-abs(x1-x2))*(h2-abs(y1-y2)))
    else :
        if y1 <= y2 :
            print((w2-abs(x1-x2))*(h1-abs(y1-y2)))
        else :
            print((w2-abs(x1-x2))*(h2-abs(y1-y2)))
main()
