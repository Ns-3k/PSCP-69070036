"""3395"""
def main():
    """wha"""
    n, l = map(int, input().split())
    heights = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    max_height = 0*l
    for i in range(n):
        if i + 1 in customers:
            print(max(0, max_height - heights[i] + 1))
        max_height = max(max_height, heights[i])
main()
