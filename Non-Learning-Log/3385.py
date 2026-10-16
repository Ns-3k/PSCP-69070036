"""3385"""
def main():
    """bstop"""
    p = int(input())
    n = int(input())
    bus = []
    count = 0
    stops = {}
    for _ in range(n):
        temp = list(map(int, input().split()))
        stops[temp[0]] = temp[1:]
    for stop in range(1, n + 1):
        count += bus.count(stop)
        bus = [i for i in bus if i != stop]
        for i in stops[stop]:
            if i > stop and len(bus) < p:
                bus.append(i)
    print(count)
main()
