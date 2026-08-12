"""3058"""
def main():
    """beeeeeek"""
    a = int(input())
    b = int(input())
    goal = int(input())
    done  = 0
    if goal >= 5 and b:
        if b*5 > goal:
            b = goal//5
        goal -= 5*b
    if not goal:
        print(0)
        done = 1
    if goal and a:
        a = min(a,goal)
        goal -= a
    if goal:
        print(-1)
    elif not done:
        print(a)
main()
