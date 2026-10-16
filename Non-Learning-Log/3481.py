"""3481"""
def main():
    """saparn"""
    l, n = map(int, input().split())
    bridges = []
    for _ in range(n):
        a, b = map(int, input().split())
        bridges.append((a, b))
    max_bridges = 0
    for x in range(l * 2 + 1):
        pos = x / 2
        count = 0
        for a, b in bridges:
            if a < pos < b:
                count += 1
        max_bridges = max(max_bridges, count)
    print(max_bridges)
main()
