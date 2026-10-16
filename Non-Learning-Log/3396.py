"""3396"""
def main():
    """run"""
    n, k = map(int, input().split())
    times = [int(input()) for _ in range(n)]
    fast = min(times)
    count = 0
    for t in times:
        if k == 1 or (k - 1)*t < k *fast:
            count += 1
    print(count)
main()
