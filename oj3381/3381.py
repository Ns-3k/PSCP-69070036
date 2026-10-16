"""3381"""
def main():
    """sort"""
    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        point = []
        for _ in range(n):
            point.append(list(map(int,input().split())))
        point.sort(key=lambda x: (x[0]+x[1], -x[1]))
        for i in point:
            ans.append(i)
    for i in (ans):
        print(*i)
main()
