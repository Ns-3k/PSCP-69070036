"""3232"""
def main():
    """frog"""
    jump = input().split()
    dis = 0
    count = 0
    while dis < int(jump[1]):
        dis += int(jump[0])-2*count
        if int(jump[0])-2*count <= 0:
            print(-1)
            return
        count += 1
    print(count)
main()
