"""3383"""
def main():
    """difff"""
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    for _ in range(n):
        a.add(int(input()))
    for _ in range(m):
        b.add(int(input()))
    ans = sorted(a - b)
    print(*ans)
main()
