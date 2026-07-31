"""3035"""
import math as m
def main():
    """filter"""
    cord = input().split(" ")
    d = m.pow(m.pow(int(cord[1]),2)+m.pow(int(cord[2]),2),0.5)
    r = int(cord[0])
    if d > r:
        print("OUT")
    elif d == r:
        print("ON")
    else:
        print("IN")
main()
