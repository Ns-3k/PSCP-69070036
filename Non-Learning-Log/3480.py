"""3480"""
def main():
    """birb"""
    n = int(input())
    heights = list(map(int, input().split()))
    count = 0
    if n == 1:
        print(1)
        return
    for i in range(n):
        if not i:
            if heights[i] > heights[i + 1]:
                count += 1
        elif i == n - 1:
            if heights[i] > heights[i - 1]:
                count += 1
        elif heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            count += 1
    print(count)
main()
