"""3360"""
def main():
    """bread>key"""
    w,h,x,y = map(int,input().split())
    blade_x = list(map(int,input().split()))
    blade_y = list(map(int,input().split()))
    blade_x.append(w)
    blade_y.append(h)
    for i in range(1,x+1):
        blade_x[-i] -= blade_x[-i-1]
    for i in range(1,y+1):
        blade_y[-i] -= blade_y[-i-1]
    blade_x.sort()
    blade_y.sort()
    print(blade_x[-1]*blade_y[-1],max(blade_y[-1]*blade_x[-2],blade_y[-2]*blade_x[-1]))
main()
