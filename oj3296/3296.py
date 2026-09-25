"""3296"""
def main():
    """rgbbbgrrrb"""
    rgb1 = list(map(int,input().split()))
    rgb2 = list(map(int,input().split()))
    rgb3 = [int((rgb1[0]+rgb2[0])/2),int((rgb1[1]+rgb2[1])/2),int((rgb1[2]+rgb2[2])/2)]
    print(*rgb3)
main()
