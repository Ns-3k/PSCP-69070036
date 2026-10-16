"""3387"""
def main():
    """tup"""
    x = list(input().split())
    tup = tuple(x)
    y  = input()
    for _ in range(tup.count(y)):
        for i in range(tup.count(y)):
            if i != tup.count(y)-1:
                print(tup.index(y),end=" ")
            else:
                print(tup.index(y))
main()
