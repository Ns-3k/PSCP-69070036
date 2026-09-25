"""3236"""
def main():
    """id"""
    n = int(input())
    id1 = input()
    id2 = input()
    count = 0
    for i in range(n):
        if int(id1[i])+int(id2[i]) != 9:
            count += 1
            if count == 1:
                print("NO",end=" ")
    if not count:
        print("YES")
    else:
        print(count)
main()
