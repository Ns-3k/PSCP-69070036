"""INK"""
import math as m
def main():
    """asdasd"""
    first=input().split(" ")
    growth=float(first[0])
    request=int(first[1])
    time=0
    for _ in range(request):
        home=str(input()).split(" ")
        x=int(home[0])
        y=int(home[1])
        r=m.pow(m.pow(x,2)+m.pow(y,2),0.5)
        area=3.1416*(m.pow(r,2))
        time=area/growth
        if time%1:
            time = time//1 + 1
        if not x and not y:
            print(0)
        else:
            print(int(time))
main()
