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
    width = min(x1+w1,x2+w2)-max(x1,x2)
    height = min(y1+h1,y2+h2)-max(y1,y2)
    if x1+w1 <= x2 or y1+h1 <= y2:
        print("no overlapping")
    else:
        print(width*height)
main()
