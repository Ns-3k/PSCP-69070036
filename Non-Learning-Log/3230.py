"""3230"""
import math
def stdigit(n):
    """1st digit"""
    if n[0] > 5:
        room = "9"
    elif n[1] > 5:
        room = "10"
    elif n[2] > 5:
        room = "11"
    elif n[3] > 5:
        room = "12"
    elif n[4] > 5:
        room = "14"
    else:
        room = "13"
    return room
def nddigit(n):
    """2nd digit"""
    if n == n[::-1]:
        if n[0]+n[4] > 5:
            room = "1"
        elif n[1]*n[3] > 5:
            room = "2"
        else:
            room = "0"
    else:
        if n[4]:
            if n[0]//n[4] > 5:
                room = "1"
        if n[1]-n[4] > 5:
            room = "2"
        else:
            room = "0"
    return room
def rddigit(n):
    """3rd digit"""
    if sum(n) > 25:
        room = "1"
    elif math.prod(n) > 55:
        room = "2"
    else:
        room = "0"
    return room
def main():
    """hotel"""
    n = []
    temp = input()
    for i in range (5):
        n.append(int(temp[i]))
    room = ""
    room += stdigit(n)
    room += nddigit(n)
    room += rddigit(n)
    print(room)
main()
