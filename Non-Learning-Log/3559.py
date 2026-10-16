"""3559"""
def main():
    """charmๆ"""
    n = int(input())
    max_count = 0
    charm = []
    for _ in range (n):
        charm.append(int(input()))
    for i in range (1,301):
        count = charm.count(i)
        max_count = max(max_count,count)
    print(max_count)
main()
