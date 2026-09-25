"""3299"""
def main():
    """garden"""
    l,n = map(int,input().split())
    count = 0
    plant = 0
    while plant < n:
        count += 1
        if count == 1:
            plant += ((l*(l+1))//2)
        else:
            plant += ((l*(l+1))//2) + (count-1)*(l**2)
    print(count)
main()
