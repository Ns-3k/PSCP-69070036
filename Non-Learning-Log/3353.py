"""3353"""
def main():
    """3or5"""
    numlist = list(map(int,input().split()))
    ans = []
    for i in numlist:
        if not i%3 or not i%5:
            ans.insert(0,i)
    if ans:
        print(*ans,sep="\n")
    else:
        print("Nope")
main()
