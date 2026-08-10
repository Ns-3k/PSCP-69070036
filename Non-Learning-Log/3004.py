"""3004"""
def main():
    """quadratic"""
    point1 = input().split(" ")
    point2 = input().split(" ")
    x = (int(point1[0])-int(point2[0]))**2
    y = (int(point1[1])-int(point2[1]))**2
    z = (int(point1[2])-int(point2[2]))**2
    distance = (x+y+z)**0.5
    print(f"{distance:.2f}")
main()
