"""3034"""
def main():
    """pod"""
    n, k = map(int, input().split())
    count = [0] * (k+1)
    for _ in range(n):
        psg = int(input())
        count[psg] += 1
    group = min(count[1:])
    print(n - group*k)
main()
