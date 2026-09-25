"""3293"""
def main():
    """frame"""
    line = []
    for _ in range(5):
        line.append(input().strip())
    frame = len(max(line,key=len))
    print("*"*(frame+4))
    for i in range(5):
        print("*",line[i]+" "*(frame-len(line[i])),"*")
    print("*"*(frame+4))
main()
