"""3358"""
def main():
    """piGG"""
    n  = int(input())
    big = []
    total = 0
    pigs = list(map(int,input().split()))
    for i in range(n):
        total += max(pigs[0+2*i],pigs[1+2*i])
        big.append(max(pigs[0+2*i],pigs[1+2*i]))
    if len(big) > 1:
        print(*big,sep=" + ",end=" = ")
        print(total)
    else:
        print(*big)
main()
