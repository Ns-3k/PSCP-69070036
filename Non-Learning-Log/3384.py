"""3384"""
import json
def main():
    """jSON"""
    mylist = map(int,json.loads(input()))
    ans = []
    for i in mylist:
        if not i%2:
            ans.append(i)
    if ans:
        print(*ans,sep="\n")
    else:
        print("Nope")
main()
