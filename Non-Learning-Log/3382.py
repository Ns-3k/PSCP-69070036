"""3382"""
def main():
    """null"""
    temp = "sadsad"
    mylist = []
    while temp != "NULL":
        temp = input()
        mylist.append(temp)
    mylist.pop()
    while mylist:
        print(mylist.pop())
main()
