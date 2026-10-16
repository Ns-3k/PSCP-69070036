"""3386"""
def main():
    """dupe"""
    m = int(input())
    n = int(input())
    g1 = set()
    g2 = set()
    for _ in range (m):
        g1.add(input())
    for _ in range (n):
        g2.add(input())
    dupe = sorted(set(g1.intersection(g2)),reverse=True)
    if dupe:
        print(*dupe,sep="\n")
    else:
        print("Nope")
main()
