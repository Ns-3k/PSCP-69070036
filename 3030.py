"""3030"""
import math as m
def main():
    """saitama"""
    pushup = int(input())
    situp = int(input())
    squat = int(input())
    run = int(input())
    pushup1d = int(input())
    situp1d = int(input())
    run1d = int(input())
    squat1d = int(input())
    print(max(m.ceil(pushup/pushup1d),m.ceil(situp/situp1d)\
,m.ceil(squat/squat1d),m.ceil(run/run1d)))
main()
