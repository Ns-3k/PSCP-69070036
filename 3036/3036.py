"""castle"""
def main():
    """castle"""
    room = float(input())
    right_room = 1
    floor = 1
    while room > right_room:
        floor += 1
        right_room = floor**2
    if not ((floor-1)**2+1-room)%2:
        print((floor-1)*2)
    else:
        print((floor-1)*2-1)
main()
