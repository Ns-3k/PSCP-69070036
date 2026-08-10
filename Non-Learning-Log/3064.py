"""3064"""
import datetime as dt
def main():
    """bday"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    y2 = int(input())
    m2 = int(input())
    d2 = int(input())
    if abs((dt.date(y1,m1,d1) - dt.date(y2,m2,d2)).days) <= 7:
        print(0)
    elif dt.date(y1,m1,d1) < dt.date(y2,m2,d2):
        print(1)
    elif dt.date(y1,m1,d1) > dt.date(y2,m2,d2):
        print(2)
main()
